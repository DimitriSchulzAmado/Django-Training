# Generated by Django 3.1.2 on 2023-10-09 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='capital',
            field=models.BooleanField(default=False),
        ),
    ]
