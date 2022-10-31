# Generated by Django 4.1.1 on 2022-09-25 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='title',
        ),
        migrations.AddField(
            model_name='course',
            name='cdescription',
            field=models.TextField(default='Description', max_length=200),
        ),
        migrations.AddField(
            model_name='course',
            name='ctitle',
            field=models.CharField(default='Title', max_length=50),
        ),
        migrations.AlterModelTable(
            name='course',
            table='courses',
        ),
    ]
