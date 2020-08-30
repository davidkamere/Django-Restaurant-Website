# Generated by Django 3.0.5 on 2020-08-28 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20200828_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='extra_info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='header_image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='ingredients',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='instructions',
            field=models.TextField(blank=True, null=True),
        ),
    ]
