# Generated by Django 2.2.3 on 2019-07-30 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='SchedulePid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
