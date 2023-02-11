from odoo import http
from odoo.http import request
import logging

class CustomFormController(http.Controller):

    #Rota para o formulário com a lista de projetos para seleção
    #A rota é protegida por autenticação pública
    #O CSRF é desabilitado para que o formulário possa ser submetido por um usuário não logado
    @http.route('/projetos', type='http', auth='public', website=True, csrf=False)
    def create_task(self, **kwargs):
        task = None
        if kwargs.get('submit') and kwargs.get('name') and kwargs.get('message'):
            
            #Criar uma tarefa com os dados do formulário e o projeto selecionado
            task = request.env['project.task'].sudo().create({
                'name': kwargs.get('name', ''),
                'description': kwargs.get('message', ''),
                'project_id': int(kwargs.get('selected_value', '')),                            
                })
        projects = request.env['project.project'].sudo().search([])

        # Renderiza o template com os projetos
        return http.request.render('task_endpoint.form_template', {
            'task': task,
            'projects': projects,
        })

