# Generated by Django 3.1 on 2020-10-18 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorys',
            name='category',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='products',
            name='product',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]