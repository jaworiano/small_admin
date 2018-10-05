# Generated by Django 2.1.2 on 2018-10-05 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('small_admin_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArcMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.FloatField(choices=[(10.0, '10.0'), (10.1, '10.1'), (10.2, '10.2'), (10.3, '10.3'), (10.4, '10.4'), (10.5, '10.5')], default=10.0)),
                ('license', models.CharField(choices=[('B', 'BASIC'), ('S', 'STANDARD'), ('A', 'ADVANCE')], default='BASIC', max_length=10)),
            ],
        ),
    ]