# Generated by Django 2.2.5 on 2020-04-26 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='patientId',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
