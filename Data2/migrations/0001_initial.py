# Generated by Django 4.2.5 on 2024-01-09 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('image', models.FileField(default=None, max_length=330, null=True, upload_to='')),
            ],
        ),
    ]
