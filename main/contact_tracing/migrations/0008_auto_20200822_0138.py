# Generated by Django 3.1 on 2020-08-21 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_tracing', '0007_auto_20200818_1133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locationlog',
            name='date',
        ),
        migrations.RemoveField(
            model_name='locationlog',
            name='time',
        ),
        migrations.AddField(
            model_name='locationlog',
            name='e_time',
            field=models.IntegerField(default='0'),
            preserve_default=False,
        ),
    ]
