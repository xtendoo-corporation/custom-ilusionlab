from odoo import models, fields, api, _


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    def _get_task_name(self):
        task_id = self.env.context.get('default_task_id')
        task_id = self.env["project.task"].search(
            [("id", "=", (task_id))]
        )
        return task_id.name

    name = fields.Char('Description', required=True, default=_get_task_name)


