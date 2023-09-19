# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class Projectphase(models.Model):
    _name = "project.phase"
    _description = "Project Phase"
    _rec_name = "complete_name"

    parent_id = fields.Many2one(comodel_name="project.phase", string="Parent Phase")
    child_ids = fields.One2many(
        comodel_name="project.phase", inverse_name="parent_id", string="Subphases"
    )
    name = fields.Char(required=True, translate=True)
    complete_name = fields.Char(
        compute="_compute_complete_name", store=True, recursive=True
    )
    description = fields.Text(translate=True)
    project_ok = fields.Boolean(string="Can be applied for projects", default=True)
    task_ok = fields.Boolean(string="Can be applied for tasks")
    code = fields.Char(copy=False)

    @api.constrains("parent_id")
    def check_parent_id(self):
        if not self._check_recursion():
            raise ValidationError(_("You cannot create recursive project phases."))

    @api.depends("name", "parent_id.complete_name")
    def _compute_complete_name(self):
        for project_phase in self:
            if project_phase.parent_id:
                project_phase.complete_name = "{} / {}".format(
                    project_phase.parent_id.complete_name, project_phase.name
                )
            else:
                project_phase.complete_name = project_phase.name
