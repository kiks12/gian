# Generated by Django 4.1.2 on 2022-10-30 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_user_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='courses',
            field=models.CharField(default='', max_length=2048),
        ),
    ]
