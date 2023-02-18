from django.shortcuts import render
from django.views.generic import ListView
from .models import CoursesModel


class CoursesModelView(ListView):
    template_name = 'courses.html'
    model = CoursesModel
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = CoursesModel.objects.all()
        return context
