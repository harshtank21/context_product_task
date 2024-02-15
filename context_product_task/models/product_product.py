from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    # @api.constrains('name')
    # def _check_internal_reference(self):
    #     print(self.env.context)
    #     product_name = self.default_code
    #     self.name = product_name[0:product_name.index('-')]

    @api.onchange('name')
    def _onchange_name(self):
        print(self.env.context)
        product_name = self.default_code
        self.name = product_name[0:product_name.index('-')]
