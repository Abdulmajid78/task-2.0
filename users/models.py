from django.db import models
from django.contrib.auth.models import AbstractUser


class UsersModel(AbstractUser):
    nickname = models.CharField(max_length=55)

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class StudentsModel(models.Model):
    user = models.OneToOneField(UsersModel, on_delete=models.CASCADE, related_name='student')
    address = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=16, null=True, blank=True)

    c = 'Completed'
    s = 'Student'

    statuses = [
        (c, 'Completed'),
        (s, 'Student')
    ]

    status = models.CharField(
        max_length=20,
        choices=statuses,
        default=s,
    )

    def status_selector(self):
        return self.status in (self.s, self.c)

    def get_full_name(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'


class TeacherDirectionsModel(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return  self.name

    class Meta:
        verbose_name  = 'direction'
        verbose_name_plural = 'directions'


class TeachersModel(models.Model):
    user = models.OneToOneField(UsersModel, on_delete=models.CASCADE, related_name='teacher')
    direction = models.ForeignKey(TeacherDirectionsModel, on_delete=models.RESTRICT, related_name='teacher')
    address = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=16, null=True, blank=True)

    def get_full_name(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'teacher'
        verbose_name_plural = 'teacher'