# Generated by Django 3.1.1 on 2020-10-26 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201026_0622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='image',
            field=models.ForeignKey(blank=True, default=2, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dish_image', to='main.image'),
        ),
    ]
