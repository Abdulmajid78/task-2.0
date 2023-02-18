
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentsmodel',
            old_name='users',
            new_name='user',
        ),
    ]
