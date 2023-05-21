# Generated by Django 4.2 on 2023-05-21 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pengguna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('nim', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'pengguna',
            },
        ),
    ]
