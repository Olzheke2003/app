from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'recruitment_agency/index.html'
    title = 'Recruitment agency'

