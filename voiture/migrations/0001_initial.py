# Generated by Django 5.0.6 on 2024-05-21 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricule', models.CharField(max_length=40)),
                ('marque', models.CharField(max_length=40)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('kelometrage', models.DecimalField(decimal_places=2, max_digits=10)),
                ('disponibilite', models.BooleanField(default=True)),
            ],
        ),
    ]
