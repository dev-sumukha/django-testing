# Generated by Django 4.1.2 on 2022-11-02 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='card_img',
            field=models.ImageField(default=0, upload_to='media/carding/%Y'),
            preserve_default=False,
        ),
    ]