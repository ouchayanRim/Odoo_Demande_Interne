from odoo import models, fields

class DemandeInterne(models.Model):
    _name = 'demande.interne'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Gestion des demandes internes'

    name = fields.Char(string='Objet', required=True)
    description = fields.Text(string='Description')
    date_creation = fields.Date(string='Date', default=fields.Date.context_today)
    priorite = fields.Selection([
        ('0', 'Basse'),
        ('1', 'Moyenne'),
        ('2', 'Haute')
    ], string='Priorité', default='1')
    
    user_id = fields.Many2one('res.users', string='Responsable')
    date_deadline = fields.Date(string='Date limite')
    tag_ids = fields.Many2many('demande.tag', string='Étiquettes')
    color = fields.Integer(string='Couleur')
    
    etat = fields.Selection([
        ('brouillon', 'Brouillon'),
        ('envoye', 'Envoyé'),
        ('termine', 'Terminé')
    ], string='Statut', default='brouillon', tracking=True)

    def action_envoyer(self):
        self.etat = 'envoye'

    def action_terminer(self):
        self.etat = 'termine'

    def action_brouillon(self):
        self.etat = 'brouillon'