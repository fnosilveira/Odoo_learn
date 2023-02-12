from requests import post
from odoo import http
from odoo.http import request
import logging
import base64


class CustomFormController(http.Controller):

    # Rota para o formulário com a lista de projetos para seleção
    # A rota é protegida por autenticação pública
    # O CSRF é desabilitado para que o formulário possa ser submetido por um usuário não logado

    @http.route('/projetos', type='http', auth='public', website=True, csrf=False, methods=['GET', 'POST'])
    def create_task(self, **kwargs):
        task = None
        if kwargs.get('submit'):

            # Criar uma tarefa com os dados do formulário e o projeto selecionado
            task = request.env['project.task'].sudo().create({
                'name': kwargs.get('name', ''),
                'description': kwargs.get('message', ''),
                'project_id': int(kwargs.get('selected_value', '')),
            })

            # Envia uma notificação para o usuário, avisando a origem da tarefa
            task.message_post(
                body="Esta tarefa foi criada por um usuário externo."
            )

            # ToDo - Enviar o anexo do formulário para o Odoo
            





            # Redireciona para o template de sucesso
            return http.request.render('task_endpoint.success_template', {
                'task': task,
            })

        projects = request.env['project.project'].sudo().search([])

        # Renderiza o template com os projetos
        return http.request.render('task_endpoint.form_template', {
            'task': task,
            'projects': projects,
        })
    
