# Generated by Django 3.1 on 2020-11-04 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_auto_20201104_1620"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="date_joined",
            field=models.DateField(auto_now_add=True),
        ),
    ]