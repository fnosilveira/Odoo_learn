# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Form(models.Model):
    _name = 'form.form'
    _description = 'Form'

    #Define os campos usados no formulário

    campaign_name = fields.Char(string="Campaign Name")
    campaign_type = fields.Selection([ ('1', 'Lançamento'),
        ('2', 'Branding'),
        ('3', 'Comercial(aumento de ticket)'),
        ('4', 'Comercial(aumento de fluxo)'),
        ('5', 'Encantamento'), 
        ('6', 'Reativação')],
        string="Campaign Type")
    campaign_year = fields.Selection([ ('1', '2021'),
        ('2', '2022'),
        ('3', '2023')],
        string="Campaign Year")
    campaign_brief = fields.Text(string="Campaign Brief")
    campaign_validity = fields.Date(string="Campaign Validity")
    project_id = fields.Many2one('project.project', string="Project")
    

    #Cria a tarefa com os campos do formulário

    def create_task(self):
        task = self.env['project.task'].create({
            'name': self.campaign_name,
            #Levando para o campo descrição somente o campo Brief
            'description': self.campaign_brief,
            'project_id': self.project_id.id,
        })
        return task