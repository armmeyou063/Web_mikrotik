# Generated by Django 2.2.5 on 2022-04-26 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0007_vlans_tagged1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vlans',
            name='tagged1',
        ),
    ]