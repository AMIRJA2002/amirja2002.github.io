# Generated by Django 5.0 on 2023-12-27 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_exceldata_row'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exceldata',
            name='engine_power',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='exceldata',
            name='engine_serial_number',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='exceldata',
            name='floor',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='exceldata',
            name='serial_number',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
