from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class system_stewart_platform(models.Model):
    title = models.CharField('Наименование системы', max_length=50)
    discription_system = models.TextField('Описание системы')

    LAW_TYPE=(
        ('Волна', 'Волна'),
        ('Колебания', 'Колебания'),
    )

    law_system = models.CharField(verbose_name='Закон движения системы', max_length=10, choices=LAW_TYPE, null=False,
                blank=True, default='Волна', help_text='')
    x_max_matrix = models.IntegerField('Размер матрицы по оси x')
    y_max_matrix = models.IntegerField('Размер матрицы по оси y')
    author = models.ForeignKey(User, related_name='system_stewart_platform_user_created',
                                            verbose_name=u'Пользователь', on_delete=models.CASCADE, null=True,
                                            blank=True, default=None)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Добавлено")  # YYYY-MM-DD HH:MM
    time_update = models.DateTimeField(auto_now=True, verbose_name="Изменено")

    def _str_(self):
        return self.title

    def get_absolute_url(self):
        return reverse('systemDetailView', args=[str(self.id)])

    class Meta:
        verbose_name = 'Система Stewart Platform'
        verbose_name_plural = 'Системы Stewart Platform'


class stewart_platform(models.Model):
    system_stewart_platform= models.ForeignKey(system_stewart_platform, verbose_name='Система', on_delete=models.CASCADE)
    title = models.CharField('Наименование базового модуля', max_length=50)
    discription = models.TextField('Описание базового модуля')
    ip_adress = models.GenericIPAddressField('IP адрес', protocol='both', unpack_ipv4=False)
    port = models.PositiveSmallIntegerField('Порт подключения', default=0)
    position_x_in_matrix = models.IntegerField('Позиция базового модуля в матрице по оси х')
    position_y_in_matrix = models.IntegerField('Позиция базового модуля в матрице по оси у')
    author = models.ForeignKey(User, related_name='stewart_platform_user_created',
                                            verbose_name=u'Пользователь', on_delete=models.CASCADE, null=True,
                                            blank=True, default=None)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Добавлено")  # YYYY-MM-DD HH:MM
    time_update = models.DateTimeField(auto_now=True, verbose_name="Изменено")

    def _str_(self):
        return self.title

    def get_absolute_url(self):
        return reverse('platformDetailView', args=[str(self.id)])

    class Meta:
        verbose_name = 'Базовый модуль'
        verbose_name_plural = 'Базовые модули'


class law_for_platform_wave(models.Model):
    stewart_platform = models.ForeignKey(stewart_platform, verbose_name='Базовый модуль', on_delete=models.CASCADE)
    time = models.IntegerField('момент времени в секундах')
    x_coordinate = models.IntegerField('Смещение по x')
    y_coordinate = models.IntegerField('Смещение по y')
    z_coordinate = models.IntegerField('Смещение по z')
    γ_roll_x = models.IntegerField('Крен(х)')
    θ_pitch_y = models.IntegerField('Тангаж(y)')
    ψ_yaw_z = models.IntegerField('Рыскание(z)')
    author = models.ForeignKey(User, related_name='law_for_platform_wave_user_created',
                                            verbose_name=u'Пользователь', on_delete=models.CASCADE, null=True,
                                            blank=True, default=None)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Добавлено")  # YYYY-MM-DD HH:MM
    time_update = models.DateTimeField(auto_now=True, verbose_name="Изменено")

    def _str_(self):
        return self.title

    def get_absolute_url(self):
        return reverse('LawWaveDetailView', args=[str(self.id)])

    class Meta:
        verbose_name = 'Закон движения для базового модуля-волна'
        verbose_name_plural = 'Законы движения для базового модуля-волна'

class law_for_platform_vibrations(models.Model):
    stewart_platform = models.ForeignKey(stewart_platform, verbose_name='Базовый модуль', on_delete=models.CASCADE)
    time = models.IntegerField('момент времени в секундах')
    x_coordinate = models.IntegerField('Смещение по x')
    y_coordinate = models.IntegerField('Смещение по y')
    z_coordinate = models.IntegerField('Смещение по z')
    γ_roll_x = models.IntegerField('Крен(х)')
    θ_pitch_y = models.IntegerField('Тангаж(y)')
    ψ_yaw_z = models.IntegerField('Рыскание(z)')
    author = models.ForeignKey(User, related_name='law_for_platform_vibrations_user_created',
                                            verbose_name=u'Пользователь', on_delete=models.CASCADE, null=True,
                                            blank=True, default=None)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Добавлено")  # YYYY-MM-DD HH:MM
    time_update = models.DateTimeField(auto_now=True, verbose_name="Изменено")

    def _str_(self):
        return self.title

    def get_absolute_url(self):
        return reverse('LawVibrationsDetailView', args=[str(self.id)])

    class Meta:
        verbose_name = 'Закон движения для базового модуль-вибрация'
        verbose_name_plural = 'Законы движения для базового модуля-вибрация'

