from odoo import models, fields

class Categorie(models.Model):
    _name = 'categorie.produit'
    _description = 'Organise les produits en catégories.'

    name = fields.Char(string="Nom", required=True)
    description = fields.Text(string="Description")