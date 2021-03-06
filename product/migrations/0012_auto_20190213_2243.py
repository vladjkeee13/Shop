# Generated by Django 2.1.5 on 2019-02-13 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20190213_1452'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.IntegerField(choices=[(0, 'Women'), (1, 'Men'), (2, 'Unisex'), (3, 'Kids')], default=2)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Category')),
                ('gender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Gender')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='gender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Gender'),
        ),
    ]
