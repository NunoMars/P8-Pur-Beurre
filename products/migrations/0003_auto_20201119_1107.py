# Generated by Django 3.1 on 2020-11-19 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_delete_history"),
    ]

    operations = [
        migrations.AlterField(
            model_name="products",
            name="nutrition_grade_fr",
            field=models.IntegerField(),
        ),
    ]
