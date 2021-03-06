# Generated by Django 2.1.5 on 2019-02-26 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0025_auto_20190226_0937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image_gender_category',
        ),
        migrations.AddField(
            model_name='brand',
            name='image_kids',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='image_kids', to='product.Image'),
        ),
        migrations.AddField(
            model_name='brand',
            name='image_men',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='image_men', to='product.Image'),
        ),
        migrations.AddField(
            model_name='brand',
            name='image_women',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='image_women', to='product.Image'),
        ),
    ]
