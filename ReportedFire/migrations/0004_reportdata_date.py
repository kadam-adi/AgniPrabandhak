# Generated by Django 4.2.5 on 2023-10-07 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportedfire', '0003_reportdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportdata',
            name='date',
            field=models.CharField(max_length=30, null=True),
        ),
    ]