# Copyright 2022 Manuel Calero (<http://xtendoo.es>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Project timesheet control Customize",
    "summary": "Project timesheet control Customize",
    "author": "Xtendoo,",
    "license": "AGPL-3",
    "website": "https://github.com/OCA/project",
    "category": "Project Management",
    "version": "14.0.1.0.0",
    "depends": [
        "project_timeline",
        "hr_timesheet",
        "project_timesheet_time_control",
    ],
    "data": [ "views/project_task_view.xml"],
    "installable": True,
    "auto_install": True,
}
