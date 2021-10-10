from odoo import models
from odoo.http import request, ALLOWED_DEBUG_MODES
from odoo.tools import str2bool


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    @classmethod
    def _handle_debug(cls):
        enabled = request.env['ir.config_parameter'].sudo().get_param('debug.enabled', default=False)
        if not enabled:
            return
        # Store URL debug mode (might be empty) into session
        alias = request.env['ir.config_parameter'].sudo().get_param('debug.alias', default='debug')
        if alias in request.httprequest.args:
            debug_mode = []
            for debug in request.httprequest.args[alias].split(','):
                if debug not in ALLOWED_DEBUG_MODES:
                    debug = '1' if str2bool(debug, debug) else ''
                debug_mode.append(debug)
            debug_mode = ','.join(debug_mode)

            # Write on session only when needed
            if debug_mode != request.session.debug:
                request.session.debug = debug_mode
