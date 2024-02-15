from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    currect = fields.Char(
        string='currect'
    )
    family_member_ids = fields.Many2many('res.partner', 'relation_table_one', 'col1', 'col2', string='Family Members')

    @api.onchange('family_member_ids')
    def _onchange_family_member_ids(self):
        context = self.env.context
        if 'default_currect' in context:
            for rec in self.family_member_ids:
                rec.currect = context.get('default_currect')
