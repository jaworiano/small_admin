# Generated by Django 2.1.2 on 2018-10-05 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('small_admin_app', '0006_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='divisions',
            name='division_number',
            field=models.IntegerField(choices=[(100, 'DESIGN'), (200, 'ENVIRONMENTAL'), (300, 'RAIL'), (400, 'BRIDGES'), (500, 'ADMIN')], default=100),
            preserve_default=False,
        ),
    ]
