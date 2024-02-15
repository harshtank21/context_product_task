from odoo import api, fields, models


class OrderLineWizard(models.TransientModel):
    _name = "order.line.wizard"

    order_line_ids = fields.Many2many('sale.order.line'
                                      , string='Order line')

    def default_get(self, fields_list):
        rec = super().default_get(fields_list)
        ids_get = self.env.context.get('active_ids')
        rec.update({
            'order_line_ids': [(fields.Command.set(ids_get))]
        })
        return rec
