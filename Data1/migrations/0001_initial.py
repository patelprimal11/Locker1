# Generated by Django 4.2.5 on 2024-01-05 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, serialize=False, verbose_name='ID')),
                ('mobile_no', models.IntegerField()),
                ('user_name', models.CharField(max_length=20, primary_key=True)),
                ('email_id', models.EmailField(max_length=50)),
                ('pin_no', models.IntegerField()),
            ],
        ),
    ]
