# Generated by Django 4.1.2 on 2022-10-10 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_rename_section_section_nameofsection'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='csection',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='courses.section'),
        ),
    ]
