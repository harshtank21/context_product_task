# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    price_view = fields.Integer('Price View')

    def action_show_date(self):
        store_map = self.order_line.mapped(lambda record: record.id)
        store_filtered = self.order_line.filtered(lambda record: record.price_unit >= (self.price_view or 0))
        return {
            'name': 'view',
            'type': 'ir.actions.act_window',
            'res_model': 'order.line.wizard',
            'view_id': self.env.ref('context_product_task.order_line_one_wizard_form_view').id,
            'view_mode': 'form',
            'view_type': 'form',
            'target': 'new',
            'context': {'active_model': 'sale.order', 'active_id': self.id,
                        'active_ids': list(rec.id for rec in store_filtered)}
        }
