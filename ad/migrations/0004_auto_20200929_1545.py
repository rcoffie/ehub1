# Generated by Django 3.0.8 on 2020-09-29 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0003_auto_20200929_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='trending',
            field=models.CharField(choices=[('New', 'New'), ('Hot', 'Hot')], default='Normal', max_length=100, null=True),
        ),
    ]
