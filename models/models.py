# -*- coding: utf-8 -*-
import logging


from openerp import models, fields, api
from openerp.exceptions import UserError, ValidationError
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT as DF

_logger = logging.getLogger(__name__)

class Asignacion(models.Model):
	_name = "product.template"
	_inherit = "product.template"

	referencia_articulo = fields.Char(string="Referencia articulo", compute="_llenado")

	@api.depends('default_code')
	def _llenado(self):
		for record in self:
			record.referencia_articulo = record.default_code