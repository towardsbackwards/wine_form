# Generated by Django 3.0.5 on 2020-04-16 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20200416_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sign',
            name='name',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Sign'),
        ),
    ]
