# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProjectProject(models.Model):
    _inherit = "project.project"

    phase_id = fields.Many2one(
        comodel_name="project.phase",
        string="phase",
        copy=False,
        domain="[('project_ok', '=', True)]",
    )
    batch_id = fields.Many2one(
        comodel_name="project.batch",
        string="batch",
        copy=False,
        domain="[('project_ok', '=', True)]",
    )

