# Generated by Django 4.0 on 2022-04-01 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='system_stewart_platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Наименование системы')),
                ('discription_system', models.TextField(verbose_name='Описание системы')),
                ('law_system', models.CharField(blank=True, choices=[('law1', 'закон движения 1'), ('law2', 'закон движения 2')], default='law1', max_length=10, verbose_name='Закон системы')),
                ('x_max_matrix', models.IntegerField(verbose_name='Размер матрицы по оси x')),
                ('y_max_matrix', models.IntegerField(verbose_name='Размер матрицы по оси y')),
            ],
            options={
                'verbose_name': 'Система Stewart Platform',
                'verbose_name_plural': 'Системы Stewart Platform',
            },
        ),
        migrations.CreateModel(
            name='stewart_platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Наименование базового модуля')),
                ('discription', models.TextField(verbose_name='Описание базового модуля')),
                ('ip_adress', models.GenericIPAddressField(verbose_name='IP адрес')),
                ('port', models.PositiveSmallIntegerField(default=0, verbose_name='Порт подключения')),
                ('position_x_in_matrix', models.IntegerField(verbose_name='Позиция базового модуля в матрице по оси х')),
                ('position_y_in_matrix', models.IntegerField(verbose_name='Позиция базового модуля в матрице по оси у')),
                ('system_stewart_platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='systemStewartPlatform.system_stewart_platform')),
            ],
            options={
                'verbose_name': 'Базовый модуль',
                'verbose_name_plural': 'Базовые модули',
            },
        ),
        migrations.CreateModel(
            name='law_for_platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField(verbose_name='момент времени в секундах')),
                ('x_coordinate', models.IntegerField(verbose_name='Координата по x')),
                ('y_coordinate', models.IntegerField(verbose_name='Координата по y')),
                ('z_coordinate', models.IntegerField(verbose_name='Координата по z')),
                ('γ_roll_x', models.IntegerField(verbose_name='Крен(х)')),
                ('θ_pitch_y', models.IntegerField(verbose_name='Тангаж(y)')),
                ('ψ_yaw_z', models.IntegerField(verbose_name='Рыскание(z)')),
                ('stewart_platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='systemStewartPlatform.stewart_platform')),
            ],
            options={
                'verbose_name': 'Закон движения для базового модуля',
                'verbose_name_plural': 'Законы движения для базового модуля',
            },
        ),
    ]
