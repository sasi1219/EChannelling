# Generated by Django 5.0.4 on 2024-06-27 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]