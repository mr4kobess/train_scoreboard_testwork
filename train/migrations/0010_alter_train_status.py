# Generated by Django 4.0.4 on 2022-05-16 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0009_alter_train_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='status',
            field=models.CharField(choices=[(None, 'Выберите статус'), ('lo', 'Идет посадка'), ('ar', 'Прибытие'), ('se', 'Отправлен'), ('de ', 'Задержан'), ('ca ', 'Отменен')], default=(None, 'Выберите статус'), max_length=3, verbose_name='Статус'),
        ),
    ]
