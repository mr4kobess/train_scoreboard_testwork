# Generated by Django 4.0.4 on 2022-05-16 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0003_rename_задержан до_train_задержан'),
    ]

    operations = [
        migrations.RenameField(
            model_name='train',
            old_name='Задержан',
            new_name='Задержан до',
        ),
        migrations.AlterField(
            model_name='train',
            name='Статус',
            field=models.CharField(choices=[(None, 'Выберите статус'), ('l', 'Идет посадка'), ('a', 'Прибытие'), ('s', 'Отправлен'), ('d ', 'Задержан'), ('c ', 'Отменен')], max_length=255),
        ),
    ]
