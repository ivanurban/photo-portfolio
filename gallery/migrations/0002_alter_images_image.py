# Generated by Django 3.2.5 on 2021-07-17 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/%Y/%m/%d/'),
        ),
    ]
