from django.db import models

from users.models import  TeachersModel, StudentsModel


class CoursesModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'




class GroupsModel(models.Model):
    course = models.ForeignKey(CoursesModel, on_delete=models.RESTRICT, related_name='group')
    name = models.CharField(max_length=55)
    teacher = models.ForeignKey(TeachersModel, on_delete=models.RESTRICT, related_name='group')
    student = models.ForeignKey(StudentsModel, on_delete=models.CASCADE)
    number_student = models.PositiveIntegerField()


    def __str__(self):
        return  self.name

    class Meta:
        verbose_name = 'group'
        verbose_name_plural = 'groups'

