# Generated by Django 4.2.3 on 2023-07-16 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='desc',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Descripción'),
        ),
    ]
