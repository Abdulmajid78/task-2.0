from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import CoursesModel, CategoriesModel
from django.views.generic import DetailView


class CoursesModelView(ListView):
    template_name = 'courses.html'
    model = CoursesModel
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = CoursesModel.objects.all()
        return context


def CategoriesView(request):
    categories = CategoriesModel.objects.all()
    return render(request, 'courses/courses.html', {'categories': categories})


def CoursesView(request, category_id):
    courses = CoursesModel.objects.filter(category=category_id)
    return render(request, 'courses/courses.html', {'courses': courses})


def course_detail(request, course_id):
    course = get_object_or_404(CoursesModel, id=course_id)
    return render(request, 'courses/course_detail.html', {'course': course})
