# Generated by Django 2.2.12 on 2020-06-08 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200608_2239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cvelem',
            name='content',
        ),
    ]
