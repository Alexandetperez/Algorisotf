# Generated by Django 4.2.3 on 2023-07-11 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_type_employee_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='nombre')),
            ],
            options={
                'verbose_name': 'categoria',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='categ',
            field=models.ManyToManyField(to='erp.category'),
        ),
    ]
