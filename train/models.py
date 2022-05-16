from django.db import models


class Train(models.Model):
    STATUS = (
        (None, 'Выберите статус'),
        ('l', 'Идет посадка'),
        ('a', 'Прибытие'),
        ('s', 'Отправлен'),
        ('d ', 'Задержан'),
        ('c ', 'Отменен'),

    )

    num = models.IntegerField(name="Номер")
    departure_city = models.ForeignKey('City', name='Город отправления', related_name='departure_city',
                                       on_delete=models.CASCADE)
    arrival_city = models.ForeignKey('City', name='Город прибытия', related_name='arrival_city',
                                     on_delete=models.CASCADE)
    departure_time = models.DateTimeField(name='Время отправления')
    arrival_time = models.DateTimeField(name='Время прибытия')
    detained_time = models.DateTimeField(name='Задержан до', blank=True, null=True)
    platform_number = models.IntegerField(name="Номер платформы")
    status = models.CharField(max_length=255, name='Статус', choices=STATUS)

    class Meta:
        verbose_name = "Поезд"
        verbose_name_plural = "Поезда"
        ordering = ("departure_time",)


class City(models.Model):
    name = models.CharField(max_length=255, name='Наименование')

    class Meta:
        verbose_name = " Город"
        verbose_name_plural = "Города"
