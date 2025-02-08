from odoo import models, fields

class Fournisseur(models.Model):
    _name = 'fournisseur.model'
    _description = 'Gérer les fournisseurs'

    name = fields.Char(string="Nom", required=True)
    phone = fields.Char(string="Téléphone", required=True)
    address = fields.Char(string="Adresse", required=True)
    email = fields.Char(string="Email")