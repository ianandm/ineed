# Generated by Django 3.0.4 on 2020-04-04 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ineed', '0002_post_phonenum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='phonenum',
            field=models.CharField(default='', max_length=15),
        ),
    ]
