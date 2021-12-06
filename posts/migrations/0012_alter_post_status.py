# Generated by Django 3.2.9 on 2021-11-22 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_alter_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('Ожидание ответа', 'Ожидание ответа'), ('Решенные', 'Решенные'), ('Нерешенные', 'Нерешенные'), ('Замороженные', 'Замороженные')], default='Ожидание ответа', max_length=20),
        ),
    ]