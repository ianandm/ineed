# Generated by Django 3.0.4 on 2020-04-08 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ineed', '0003_auto_20200404_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='myImage',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
