# Generated by Django 2.1.5 on 2019-02-14 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_auto_20190214_2040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ManyToManyField(to='product.Image'),
        ),
    ]
