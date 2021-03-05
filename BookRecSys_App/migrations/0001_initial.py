# Generated by Django 3.1.5 on 2021-02-03 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('isbn', models.CharField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=254)),
                ('author', models.CharField(max_length=254)),
                ('year', models.IntegerField()),
                ('publisher', models.CharField(max_length=254)),
                ('image_url', models.CharField(max_length=254)),
                ('rating_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=254)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='BookRecSys_App.user')),
            ],
        ),
    ]