# Generated by Django 4.1.7 on 2023-03-07 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openai_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]