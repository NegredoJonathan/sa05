# Generated by Django 5.0.3 on 2024-04-16 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('nascimento', models.DateTimeField()),
                ('email', models.CharField(max_length=100)),
                ('countryToWork', models.CharField(max_length=100)),
            ],
        ),
    ]
