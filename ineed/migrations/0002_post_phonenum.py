# Generated by Django 3.0.4 on 2020-03-28 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ineed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='phonenum',
            field=models.CharField(default='111 222 2222', max_length=15),
        ),
    ]
