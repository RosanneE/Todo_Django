# Generated by Django 4.0.5 on 2022-06-02 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icons', '0002_rename_list_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_name', models.CharField(max_length=200)),
                ('list_description', models.CharField(max_length=200)),
            ],
        ),
    ]
