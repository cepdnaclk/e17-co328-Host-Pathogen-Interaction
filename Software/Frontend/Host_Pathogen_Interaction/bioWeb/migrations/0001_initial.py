# Generated by Django 4.0.2 on 2022-02-28 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=40, unique=True)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
