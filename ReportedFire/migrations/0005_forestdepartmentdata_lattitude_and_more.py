# Generated by Django 4.2.5 on 2023-10-08 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportedfire', '0004_reportdata_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='forestdepartmentdata',
            name='lattitude',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='forestdepartmentdata',
            name='longitude',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
