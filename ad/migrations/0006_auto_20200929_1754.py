# Generated by Django 3.0.8 on 2020-09-29 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0005_auto_20200929_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='option',
        ),
        migrations.AddField(
            model_name='ad',
            name='status',
            field=models.CharField(choices=[('publish', 'Publish'), ('Pending', 'Pending')], default='Pending', max_length=100, null=True),
        ),
    ]
