# Generated by Django 2.2.5 on 2022-04-26 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0009_dhcpclient_dhcpnetwork_dhcpserver_ipaddress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dhcpclient',
            old_name='gateway',
            new_name='route',
        ),
    ]