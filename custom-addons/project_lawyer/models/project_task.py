# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models

class ProjectTask(models.Model):
    _inherit = "project.task"

    phase_id = fields.Many2one(
        comodel_name="project.phase", string="Phase", domain="[('task_ok', '=', True)]"
    )
    batch_id = fields.Many2one(
        comodel_name="project.batch", string="Batch", domain="[('task_ok', '=', True)]"
    )
#     batch_id = fields.Many2many(
#         comodel_name="project.batch",
#         relation="project_batch_rel",
#         column1='task_id', column2='batch_id',
#         string="Batches",
#         copy=False,
#         domain="[('project_ok', '=', True)]",
#         help="Select one or more batches for this project.",
#         #widget="many2many_tags",
# )
