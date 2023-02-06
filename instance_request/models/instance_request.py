# -*- coding: utf-8 -*-

from odoo import models, fields


class InstanceRequest(models.Model):
    _name = 'instance.request'

    NAME = fields.Char(string="DESIGNATION", required=True)
    IP = fields.Char(string="ADRESSIP", required=True)
    CPU = fields.Char(string="CPU", required=True)
    RAM = fields.Char(string="RAM", required=True)
    ACTIVE = fields.Boolean(string="ACTIVE", required=True, default=False)
    STATE = fields.Selection([('Brouillon','Brouillon'),('Soumise','Soumise'),('En traitement','En traitement'),('Traitée','Traitée')], string="STATUT", default="Brouillon")
    DISK = fields.Char(string="DISK", required=True)
    URL = fields.Char(string="URL", required=True)
    LIMIT_DATE = fields.Date(string="DATE LIMITE DE TRAITEMENT", required=True)
    TRAITEMENT_DATE = fields.Date(string="DATE DE TRAITEMENT", required=True)
    TRAITEMENT_DURATION = fields.Float(string="DUREE DE TRAITEMENT", required=True)

    def action_brouillon(self):
        for record in self:
            record.STATE = "Brouillon"

    def action_soumise(self):
        for record in self:
            record.STATE = "Soumise"

    def action_en_traitement(self):
        for record in self:
            record.STATE = "En traitement"

    def action_traiter(self):
        for record in self:
            record.STATE = "Traitée"

    