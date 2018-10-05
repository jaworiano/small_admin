# Generated by Django 2.1.2 on 2018-10-05 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('small_admin_app', '0003_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='division',
            field=models.CharField(choices=[(100, 'DESIGN'), (200, 'ENVIRONMENTAL'), (300, 'RAIL'), (400, 'BRIDGES'), (500, 'ADMIN')], default='000', max_length=36),
        ),
    ]
