# Generated by Django 4.0.3 on 2022-03-28 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=2000)),
                ('description', models.CharField(max_length=50)),
                ('auteur', models.CharField(max_length=50)),
                ('format', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('genre', models.IntegerField()),
            ],
        ),
    ]