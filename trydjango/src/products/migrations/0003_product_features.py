# Generated by Django 2.0.7 on 2019-08-07 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20190807_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='features',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
