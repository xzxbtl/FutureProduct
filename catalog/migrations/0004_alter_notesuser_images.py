# Generated by Django 5.0.6 on 2024-06-01 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_notesuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notesuser',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='users_orders', verbose_name='Изображения'),
        ),
    ]
