# Generated by Django 4.0.4 on 2022-09-19 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolname', models.CharField(max_length=100)),
                ('schooladdress', models.CharField(max_length=100)),
                ('contact', models.IntegerField(max_length=10)),
                ('pimage', models.ImageField(blank=True, upload_to='pimages')),
            ],
        ),
    ]