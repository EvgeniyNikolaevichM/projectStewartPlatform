# Generated by Django 4.0 on 2022-05-31 09:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('systemStewartPlatform', '0007_law_for_platform_vibrations_author_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='law_for_platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('law_type_plat', models.CharField(max_length=50, verbose_name='Наименование типа закона')),
                ('amplitude', models.IntegerField(verbose_name='Амплитуда закона от 0 до 100')),
                ('coordinates_t', models.JSONField(verbose_name='Координаты и параметры для платформы')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Изменено')),
                ('author', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='law_for_platform_wave_user_created', to='auth.user', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Закон движения для базового модуля',
                'verbose_name_plural': 'Законы движения для базового модуля',
            },
        ),
        migrations.RemoveField(
            model_name='law_for_platform_wave',
            name='author',
        ),
        migrations.RemoveField(
            model_name='law_for_platform_wave',
            name='stewart_platform',
        ),
        migrations.RenameField(
            model_name='stewart_platform',
            old_name='port',
            new_name='port_platform',
        ),
        migrations.RenameField(
            model_name='stewart_platform',
            old_name='title',
            new_name='title_platform',
        ),
        migrations.RenameField(
            model_name='system_stewart_platform',
            old_name='title',
            new_name='title_system',
        ),
        migrations.RemoveField(
            model_name='stewart_platform',
            name='discription',
        ),
        migrations.RemoveField(
            model_name='system_stewart_platform',
            name='law_system',
        ),
        migrations.AddField(
            model_name='stewart_platform',
            name='discription_platform',
            field=models.CharField(default=django.utils.timezone.now, max_length=500, verbose_name='Описание базового модуля'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='system_stewart_platform',
            name='law_type_system',
            field=models.CharField(blank=True, choices=[('Волна', 'Волна'), ('Колебания', 'Колебания')], default='Волна', help_text='Выбрать из списка', max_length=50, verbose_name='Закон движения системы'),
        ),
        migrations.AlterField(
            model_name='system_stewart_platform',
            name='discription_system',
            field=models.CharField(max_length=500, verbose_name='Описание системы'),
        ),
        migrations.DeleteModel(
            name='law_for_platform_vibrations',
        ),
        migrations.DeleteModel(
            name='law_for_platform_wave',
        ),
        migrations.AddField(
            model_name='law_for_platform',
            name='stewart_platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='systemStewartPlatform.stewart_platform', verbose_name='Базовый модуль'),
        ),
    ]
