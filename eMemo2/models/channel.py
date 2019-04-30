from odoo import models, fields, api
from odoo import exceptions
from odoo.exceptions import ValidationError


import logging
_logger = logging.getLogger(__name__)


class channel (models.Model):
    _name = 'x_channels'
    x_name = fields.Char(string="Channel", required=False, index=False, track_visibility=False)
