from django.db import models


class system_stewart_platform(models.Model):
    title = models.CharField('Наименование системы', max_length=50)
    discription_system = models.TextField('Описание системы')
    # LAW_TYPE=(
    #     ('law1', 'закон движения 1'),
    #     ('law2', 'закон движения 2'),
    # )
    # law_system = models.CharField(verbose_name="Закон системы", max_length=10, choices=LAW_TYPE, null=False,
    #             blank=True, default='law1', help_text='')
    law_system = models.TextField('Закон движения системы')
    x_max_matrix = models.IntegerField('Размер матрицы по оси x')
    y_max_matrix = models.IntegerField('Размер матрицы по оси y')

    def _str_(self):
        return self.title

    class Meta:
        verbose_name = 'Система Stewart Platform'
        verbose_name_plural = 'Системы Stewart Platform'


class stewart_platform(models.Model):
    system_stewart_platform= models.ForeignKey(system_stewart_platform, on_delete=models.CASCADE)
    title = models.CharField('Наименование базового модуля', max_length=50)
    discription = models.TextField('Описание базового модуля')
    ip_adress = models.GenericIPAddressField('IP адрес', protocol='both', unpack_ipv4=False)
    port = models.PositiveSmallIntegerField('Порт подключения', default=0)
    position_x_in_matrix = models.IntegerField('Позиция базового модуля в матрице по оси х')
    position_y_in_matrix = models.IntegerField('Позиция базового модуля в матрице по оси у')

    def _str_(self):
        return self.title

    class Meta:
        verbose_name = 'Базовый модуль'
        verbose_name_plural = 'Базовые модули'


class law_for_platform(models.Model):
    stewart_platform = models.ForeignKey(stewart_platform, on_delete=models.CASCADE)
    time = models.IntegerField('момент времени в секундах')
    x_coordinate = models.IntegerField('Координата по x')
    y_coordinate = models.IntegerField('Координата по y')
    z_coordinate = models.IntegerField('Координата по z')
    γ_roll_x = models.IntegerField('Крен(х)')
    θ_pitch_y = models.IntegerField('Тангаж(y)')
    ψ_yaw_z = models.IntegerField('Рыскание(z)')

    def _str_(self):
        return self.title

    class Meta:
        verbose_name = 'Закон движения для базового модуля'
        verbose_name_plural = 'Законы движения для базового модуля'