# Generated by Django 2.2.6 on 2020-04-24 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageinfo',
            name='uploadImg',
            field=models.ImageField(default='', upload_to='media/image/images'),
        ),
    ]
