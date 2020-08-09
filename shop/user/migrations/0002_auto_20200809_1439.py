# Generated by Django 3.1 on 2020-08-09 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_no',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to='media/img'),
        ),
    ]
