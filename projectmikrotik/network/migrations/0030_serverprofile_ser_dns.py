# Generated by Django 2.2.5 on 2022-04-30 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0029_remove_serverprofile_ser_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='serverprofile',
            name='ser_dns',
            field=models.CharField(default='', max_length=45),
            preserve_default=False,
        ),
    ]
