# Generated by Django 4.2 on 2023-07-13 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0010_alter_vazifamodel_foydalanuvchi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vazifamodel',
            name='foydalanuvchi',
        ),
    ]
