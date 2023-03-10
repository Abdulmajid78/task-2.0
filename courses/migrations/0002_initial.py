# Generated by Django 4.1.7 on 2023-02-18 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupsmodel',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.studentsmodel'),
        ),
        migrations.AddField(
            model_name='groupsmodel',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='group', to='users.teachersmodel'),
        ),
        migrations.AddField(
            model_name='coursesmodel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='courses.categoriesmodel'),
        ),
    ]
