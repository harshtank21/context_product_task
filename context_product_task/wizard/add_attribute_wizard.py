from odoo_16.odoo import api, fields, models


class ProductTemplateAttributeAdd(models.TransientModel):
    _inherit = "product.template.attribute.add"

    attribute_name = fields.Char(
        string='Attribute Name'
    )



