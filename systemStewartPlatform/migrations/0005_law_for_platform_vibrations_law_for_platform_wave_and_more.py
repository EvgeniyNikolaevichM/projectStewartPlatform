# Generated by Django 4.0 on 2022-04-07 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('systemStewartPlatform', '0004_alter_system_stewart_platform_law_system'),
    ]

    operations = [
        migrations.CreateModel(
            name='law_for_platform_vibrations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField(verbose_name='момент времени в секундах')),
                ('x_coordinate', models.IntegerField(verbose_name='Смещение по x')),
                ('y_coordinate', models.IntegerField(verbose_name='Смещение по y')),
                ('z_coordinate', models.IntegerField(verbose_name='Смещение по z')),
                ('γ_roll_x', models.IntegerField(verbose_name='Крен(х)')),
                ('θ_pitch_y', models.IntegerField(verbose_name='Тангаж(y)')),
                ('ψ_yaw_z', models.IntegerField(verbose_name='Рыскание(z)')),
                ('stewart_platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='systemStewartPlatform.stewart_platform')),
            ],
            options={
                'verbose_name': 'Закон движения для базового модуль-вибрация',
                'verbose_name_plural': 'Законы движения для базового модуля-вибрация',
            },
        ),
        migrations.CreateModel(
            name='law_for_platform_wave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField(verbose_name='момент времени в секундах')),
                ('x_coordinate', models.IntegerField(verbose_name='Смещение по x')),
                ('y_coordinate', models.IntegerField(verbose_name='Смещение по y')),
                ('z_coordinate', models.IntegerField(verbose_name='Смещение по z')),
                ('γ_roll_x', models.IntegerField(verbose_name='Крен(х)')),
                ('θ_pitch_y', models.IntegerField(verbose_name='Тангаж(y)')),
                ('ψ_yaw_z', models.IntegerField(verbose_name='Рыскание(z)')),
                ('stewart_platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='systemStewartPlatform.stewart_platform')),
            ],
            options={
                'verbose_name': 'Закон движения для базового модуля-волна',
                'verbose_name_plural': 'Законы движения для базового модуля-волна',
            },
        ),
        migrations.AlterField(
            model_name='system_stewart_platform',
            name='law_system',
            field=models.CharField(blank=True, choices=[('Волна', 'Волна'), ('Колебания', 'Колебания')], default='Волна', max_length=10, verbose_name='Закон движения системы'),
        ),
        migrations.DeleteModel(
            name='law_for_platform',
        ),
    ]