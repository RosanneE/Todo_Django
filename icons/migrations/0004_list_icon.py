# Generated by Django 4.0.5 on 2022-06-02 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icons', '0003_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='icon',
            field=models.ManyToManyField(to='icons.icon'),
        ),
    ]