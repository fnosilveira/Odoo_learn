# -*- coding: utf-8 -*-
{
    'name': "form_to_task",
    'summary': "Create a task from a form",

    'description': " This module allows you to create a task from a form. ",
    'author': "Gustavo Lima",
    'category': 'Project',
    'version': '0.1',

    'depends': ['base', 'project'],

    'data': [
        #Security
        'security/ir.model.access.csv',
        #Views
        'views/form_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,

}
