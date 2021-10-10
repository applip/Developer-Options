from odoo import models, fields


class ResConfigSettings(models.TransientModel):

    _inherit = 'res.config.settings'

    enable_debug = fields.Boolean()

    debug_alias = fields.Char('Debug Alias', default='debug')

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('debug.enabled', self.enable_debug)
        self.env['ir.config_parameter'].sudo().set_param('debug.alias', self.debug_alias)

    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res.update({
            'enable_debug': self.env['ir.config_parameter'].sudo().get_param('debug.enabled'),
            'debug_alias': self.env['ir.config_parameter'].sudo().get_param('debug.alias'),
        })
        return res