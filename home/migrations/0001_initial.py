# Generated by Django 4.0 on 2021-12-19 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boardrooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('capacity', models.IntegerField(verbose_name=0)),
                ('projector', models.BooleanField(null=True)),
            ],
        ),
    ]
