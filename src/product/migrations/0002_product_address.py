# Generated by Django 5.0.2 on 2024-03-01 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
