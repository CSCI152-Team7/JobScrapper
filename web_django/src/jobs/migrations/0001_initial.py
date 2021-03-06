# Generated by Django 3.0.5 on 2020-04-26 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.DecimalField(decimal_places=10, max_digits=19)),
                ('jobTitle', models.TextField()),
                ('description', models.TextField()),
                ('place', models.TextField()),
                ('link', models.URLField()),
                ('site', models.TextField()),
            ],
        ),
    ]
