# Generated by Django 2.2.12 on 2020-06-09 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_cvelem_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cvelem',
            old_name='addDate',
            new_name='fromDate',
        ),
        migrations.AddField(
            model_name='cvelem',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='cvelem',
            name='emplyInti',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cvelem',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='cvelem',
            name='toDate',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
