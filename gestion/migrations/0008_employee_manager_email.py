# Generated by Django 5.0.7 on 2024-08-13 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0007_intervention'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='manager_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
