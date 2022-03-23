from django.db import models

class matrix(models.Model):
    position_x = models.IntegerField('Позиция платформы по оси х')
    position_y = models.IntegerField('Позиция платформы по оси y')

    def _str_(self):
        return self.title

    class Meta:
        verbose_name = 'Положение платформы в матрице'
        verbose_name_plural = 'Положения платформы в матрице'

class stewart_platform(models.Model):
    title = models.CharField('Наименование платформы', max_length=50)
    discription = models.TextField('Описание')
    ip_adress = models.GenericIPAddressField('IP адрес', protocol='both', unpack_ipv4=False)
    port = models.PositiveSmallIntegerField('Порт подключения', default=0)
    matrix = models.ForeignKey(matrix, on_delete=models.CASCADE)

    def _str_(self):
        return self.title

    class Meta:
        verbose_name = 'Базовый модуль'
        verbose_name_plural = 'Базовые модули'

class law_for_platform(models.Model):
    stewart_platform = models.ForeignKey(stewart_platform, on_delete=models.CASCADE)
    x_coordinate = models.IntegerField('Координата по x')
    y_coordinate = models.IntegerField('Координата по y')
    z_coordinate = models.IntegerField('Координата по z')
    x_rotation = models.IntegerField('Вращение по х')
    y_rotation = models.IntegerField('Вращение по y')
    z_rotation = models.IntegerField('Вращение по z')

    def _str_(self):
        return self.title

    class Meta:
        verbose_name = 'Закон движения для базового модуля'
        verbose_name_plural = 'Законы движения для базового модуля'

class law_for_system(models.Model):
    law_for_system = models.ManyToManyField(law_for_platform, verbose_name='Закон движения базового модуля')

    def _str_(self):
        return self.title

    class Meta:
        verbose_name = 'Закон движения для системы'
        verbose_name_plural = 'Законы движения для системы'

class stewart_platform_system(models.Model):
    title = models.CharField('Наименование системы', max_length=50)
    discription_sys = models.TextField('Описание')
    stewart_platform = models.ManyToManyField(stewart_platform, verbose_name='Базовый модуль в системе')
    law_sys = models.ForeignKey(law_for_system, on_delete=models.CASCADE)

    def _str_(self):
        return self.title

    class Meta:
        verbose_name = 'Система Stewart Platform'
        verbose_name_plural = 'Системы Stewart Platform'