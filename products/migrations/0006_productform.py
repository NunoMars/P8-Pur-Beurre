# Generated by Django 3.1 on 2020-10-20 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20201018_1848'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductForm',
            fields=[
                ('cherched_product', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
    ]