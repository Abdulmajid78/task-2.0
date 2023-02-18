from django.urls import path
from .views import CategoriesView, CoursesView

urlpatterns = [
    path('categories/', CategoriesView, name='categories'),
    path('courses/<int:category_id>/', CoursesView, name='courses'),
]
