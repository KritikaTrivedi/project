# Generated by Django 2.1.4 on 2019-01-08 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20190108_0531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapply',
            name='resume',
            field=models.FileField(max_length=255, upload_to='uploads/%Y/%m/%d/'),
        ),
    ]
