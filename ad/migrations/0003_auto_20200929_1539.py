# Generated by Django 3.0.8 on 2020-09-29 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0002_auto_20200928_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='option',
            field=models.CharField(choices=[('publish', 'Publish'), ('Pending', 'Pending')], max_length=100, null=True),
        ),
    ]
