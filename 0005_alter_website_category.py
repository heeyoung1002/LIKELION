# Generated by Django 3.2.4 on 2021-07-22 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20210722_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='category',
            field=models.CharField(max_length=20),
        ),
    ]
