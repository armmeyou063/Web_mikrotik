# Generated by Django 2.2.5 on 2022-04-26 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_vlans'),
    ]

    operations = [
        migrations.AddField(
            model_name='vlans',
            name='tagged1',
            field=models.CharField(default='', max_length=45),
            preserve_default=False,
        ),
    ]
