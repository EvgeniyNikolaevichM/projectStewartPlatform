# Generated by Django 4.0 on 2022-04-07 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systemStewartPlatform', '0003_alter_system_stewart_platform_law_system'),
    ]

    operations = [
        migrations.AlterField(
            model_name='system_stewart_platform',
            name='law_system',
            field=models.CharField(blank=True, choices=[('Волна', 'Волна'), ('Колебания', 'Колебания')], default='law1', max_length=10, verbose_name='Закон движения системы'),
        ),
    ]