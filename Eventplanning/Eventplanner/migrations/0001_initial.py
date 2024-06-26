# Generated by Django 5.0.4 on 2024-04-29 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Event_Name', models.CharField(default=None, max_length=100)),
                ('Event_Cost', models.IntegerField(default=0)),
                ('Event_Image', models.ImageField(upload_to='pics')),
                ('Event_Description', models.TextField(blank=True)),
            ],
        ),
    ]
