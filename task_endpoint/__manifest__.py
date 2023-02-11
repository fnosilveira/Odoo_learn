# -*- coding: utf-8 -*-
{
    'name': "Endponit Form to Task",
    'summary': "Create a task from a form in endpoint.",

    'description': " This module allows you to create a task from a form in endpoint. ",
    'author': "Gustavo Lima",
    'category': 'Project',
    'version': '0.1',

    'depends': ['base', 'project','web'],

    'data': [
        #Views
        'views/form_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,

}
