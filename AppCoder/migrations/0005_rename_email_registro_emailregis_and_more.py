# Generated by Django 4.0.1 on 2022-01-24 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0004_registro'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registro',
            old_name='email',
            new_name='emailRegis',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='fechaDeNacimiento',
            new_name='fechaDeNacimientoRegis',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='nombre',
            new_name='nombreRegis',
        ),
    ]
