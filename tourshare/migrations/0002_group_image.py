# Generated by Django 3.0.3 on 2020-02-26 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourshare', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='image',
            field=models.ImageField(default='', upload_to='tourshare/images'),
        ),
    ]
