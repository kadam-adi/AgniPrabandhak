# Generated by Django 4.2.5 on 2023-10-08 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportedfire', '0005_forestdepartmentdata_lattitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forestdepartmentdata',
            name='lattitude',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='forestdepartmentdata',
            name='longitude',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='forestdepartmentdata',
            name='phone_no',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
