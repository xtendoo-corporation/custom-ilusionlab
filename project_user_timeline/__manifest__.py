# Copyright 2022 Manuel Calero (<http://xtendoo.es>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Project User Timeline - Timesheet",
    "summary": "Shows the progress of tasks on the timeline view.",
    "author": "Xtendoo, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "website": "https://github.com/OCA/project",
    "category": "Project Management",
    "version": "14.0.1.0.0",
    "depends": [
        "project_timeline",
        "hr_timesheet"
    ],
    "data": [ "views/project_task_view.xml"],
    "installable": True,
    "auto_install": True,
}
