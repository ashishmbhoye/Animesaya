# Generated by Django 5.0.7 on 2024-08-01 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallpapers', '0003_mobile_images_alter_desktop_images_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='desktop_images',
            name='type',
            field=models.CharField(default='desktop', max_length=50),
        ),
        migrations.AddField(
            model_name='mobile_images',
            name='type',
            field=models.CharField(default='mobile', max_length=50),
        ),
    ]