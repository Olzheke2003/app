from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Jobs, Company, Category


class BrowseJobView(ListView):
    template_name = 'browse_job/jobs.html'
    title = 'Recruitment agency'
    model = Jobs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BrowseJobView, self).get_context_data(**kwargs)
        context['companies'] = Company.objects.all()
        context['categories'] = Category.objects.all()
        context['jobs'] = Jobs.objects.all()
        return context


#
#
# def job_view(request):
#     context = {
#         'title': 'Recruitment agency'
#     }
#     return render(request, 'browse_job/jobs.html', context=context)
