from odoo import models, fields, api, _


class Task(models.Model):
    _inherit = "project.task"

    project_name = fields.Char(
        string="Project name",
        related='project_id.name',
        readonly=False,
        store=True,
    )
