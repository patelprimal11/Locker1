# Generated by Django 4.2.5 on 2024-01-05 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user1',
            name='user_name',
            field=models.CharField(max_length=20),
        ),
    ]
