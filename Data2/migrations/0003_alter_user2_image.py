# Generated by Django 4.2.5 on 2024-01-09 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data2', '0002_alter_user2_image_alter_user2_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user2',
            name='image',
            field=models.FileField(default=None, max_length=330, null=True, upload_to=''),
        ),
    ]
