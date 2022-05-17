from django.db import models


class Train(models.Model):
    STATUS = (
        (None, 'Выберите статус'),
        ('lo', 'Идет посадка'),
        ('ar', 'Прибытие'),
        ('se', 'Отправлен'),
        ('de ', 'Задержан'),
        ('ca ', 'Отменен'),

    )

    num = models.CharField(verbose_name="Номер", max_length=255)
    departure_city = models.ForeignKey('City', verbose_name='Город отправления', related_name='departure_city',
                                       on_delete=models.CASCADE)
    arrival_city = models.ForeignKey('City', verbose_name='Город прибытия', related_name='arrival_city',
                                     on_delete=models.CASCADE)
    departure_time = models.DateTimeField(verbose_name='Время отправления')
    arrival_time = models.DateTimeField(verbose_name='Время прибытия')
    detained_time = models.DateTimeField(verbose_name='Задержан до', blank=True, null=True)
    platform_number = models.PositiveIntegerField(verbose_name="Номер платформы")
    status = models.CharField(max_length=3, verbose_name='Статус', choices=STATUS, default=STATUS[0])

    class Meta:
        verbose_name = "Поезд"
        verbose_name_plural = "Поезда"
        ordering = ['departure_time']

    def __str__(self):
        return f'Поезд #{self.num}'


class City(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')

    class Meta:
        verbose_name = " Город"
        verbose_name_plural = "Города"

    def __str__(self):
        return self.name
