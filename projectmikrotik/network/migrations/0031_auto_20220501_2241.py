# Generated by Django 2.2.5 on 2022-05-01 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0030_serverprofile_ser_dns'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='hotspotuser',
            new_name='users',
        ),
    ]
