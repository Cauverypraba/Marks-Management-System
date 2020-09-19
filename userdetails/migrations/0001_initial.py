# Generated by Django 3.0.5 on 2020-06-15 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('mark1', models.IntegerField(blank=True, default=0)),
                ('mark2', models.IntegerField(blank=True, default=0)),
                ('mark3', models.IntegerField(blank=True, default=0)),
            ],
        ),
    ]