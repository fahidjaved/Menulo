# Generated by Django 3.1.1 on 2020-10-26 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201025_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='order_num',
            field=models.IntegerField(default=0, verbose_name='Order Nr'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='order_num',
            field=models.IntegerField(default=0, verbose_name='Order Nr'),
        ),
        migrations.AlterField(
            model_name='sub_categories',
            name='order_num',
            field=models.IntegerField(default=0, verbose_name='Order Nr'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='order_num',
            field=models.IntegerField(default=0, verbose_name='Order Nr'),
        ),
    ]
