# Generated by Django 3.0.5 on 2020-04-27 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_auto_20200427_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobsinfo',
            name='organization',
            field=models.TextField(),
        ),
    ]
