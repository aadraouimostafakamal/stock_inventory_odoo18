from odoo import models, fields, api, exceptions

class StockMouvement(models.Model):
    _name = 'stock.mouvement'
    _description = 'Mouvements de stock.'

    product_id = fields.Many2one('stock.produits', string="Produit", required=True)
    quantity = fields.Float(string="Quantité", required=True)
    type = fields.Selection(
        [('in', 'Entrée'), ('out', 'Sortie'), ('adjust', 'Ajustement')],
        string="Type", 
        required=True
    )
    emplacement_source_id = fields.Many2one('stock.emplacement', string="Source")
    emplacement_destination_id = fields.Many2one('stock.emplacement', string="Destination")
    reason = fields.Text(string="Raison")
    date = fields.Datetime(string="Date", default=fields.Datetime.now)

    @api.constrains('type', 'quantity', 'emplacement_source_id')
    def _check_stock_availability(self):
        for mouvement in self:
            if mouvement.quantity <= 0:
                raise exceptions.ValidationError("La quantité doit être supérieure à 0.")

            if mouvement.type == 'out':
                available_qty = self.env['stock.quantity'].get_stock_quantity(
                    product_id=mouvement.product_id.id,
                    emplacement_id=mouvement.emplacement_source_id.id
                )
                if mouvement.quantity > available_qty:
                    raise exceptions.ValidationError(
                        f"Stock insuffisant. Disponible: {available_qty}"
                    )

    def _update_stock_quantity(self):
        """Update the stock quantities after a movement."""
        for mouvement in self:
            if mouvement.type == 'in':
                self.env['stock.quantity'].update_stock(
                    product_id=mouvement.product_id.id,
                    emplacement_id=mouvement.emplacement_destination_id.id,
                    quantity_change=mouvement.quantity
                )
            elif mouvement.type == 'out':
                self.env['stock.quantity'].update_stock(
                    product_id=mouvement.product_id.id,
                    emplacement_id=mouvement.emplacement_source_id.id,
                    quantity_change=-mouvement.quantity
                )
            elif mouvement.type == 'adjust':
                if mouvement.emplacement_destination_id:
                    self.env['stock.quantity'].update_stock(
                        product_id=mouvement.product_id.id,
                        emplacement_id=mouvement.emplacement_destination_id.id,
                        quantity_change=mouvement.quantity
                    )
                elif mouvement.emplacement_source_id:
                    self.env['stock.quantity'].update_stock(
                        product_id=mouvement.product_id.id,
                        emplacement_id=mouvement.emplacement_source_id.id,
                        quantity_change=-mouvement.quantity
                    )

    @api.model
    def create(self, vals):
        mouvement = super(StockMouvement, self).create(vals)
        mouvement._update_stock_quantity()
        return mouvement
