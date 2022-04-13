# Generated by Django 4.0.3 on 2022-04-13 01:26

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profesionales', '0005_surfista_folleto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surfista',
            name='folleto',
        ),
        migrations.AddField(
            model_name='surfista',
            name='tarjeta_presentacion',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]