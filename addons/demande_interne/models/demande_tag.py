from odoo import models, fields

class DemandeTag(models.Model):
    _name = 'demande.tag'
    _description = 'Étiquettes de demande'

    name = fields.Char(string='Nom', required=True)
    color = fields.Integer(string='Couleur')
