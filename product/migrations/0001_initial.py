# Generated by Django 2.1.5 on 2019-02-11 12:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('rating', models.IntegerField(default=0)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='all_images')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('price', models.PositiveSmallIntegerField(default=0)),
                ('size', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Brand')),
                ('category', models.ManyToManyField(to='product.Category')),
                ('image', models.ManyToManyField(to='product.Image')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product'),
        ),
        migrations.AddField(
            model_name='brand',
            name='image_kids',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='image_kids', to='product.Image'),
        ),
        migrations.AddField(
            model_name='brand',
            name='image_logo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='image_logo', to='product.Image'),
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
