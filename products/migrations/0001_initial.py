# Generated by Django 3.1 on 2020-10-24 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorys',
            fields=[
                ('category', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'categorys',
            },
        ),
        migrations.CreateModel(
            name='ProductForm',
            fields=[
                ('cherched_product', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('proposed_product', models.CharField(default='un_produit', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nutrition_grade_fr', models.CharField(max_length=1)),
                ('product_name_fr', models.TextField()),
                ('ingredients_text_fr', models.TextField()),
                ('product_image_large', models.TextField()),
                ('product_image_small', models.TextField()),
                ('product_image_nutrition_large', models.TextField()),
                ('product_image_nutrition_small', models.TextField()),
                ('url', models.TextField()),
                ('stores', models.TextField()),
                ('category', models.ForeignKey(default='category', on_delete=django.db.models.deletion.CASCADE, to='products.categorys')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chosen_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chosen_product', to='products.products')),
                ('remplacement_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remplacement_product', to='products.products')),
            ],
            options={
                'db_table': 'history',
            },
        ),
    ]
