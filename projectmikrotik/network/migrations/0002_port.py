# Generated by Django 2.2.5 on 2022-04-23 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='port',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port_id', models.CharField(max_length=45)),
                ('interface', models.CharField(max_length=45)),
                ('bridge', models.CharField(max_length=45)),
                ('pvid', models.CharField(max_length=45)),
                ('frametypes', models.CharField(max_length=45)),
            ],
        ),
    ]