# Generated by Django 5.0 on 2023-12-27 19:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_buildercompany_destinationcity_enginkind_origincity_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buildercompany',
            options={'verbose_name': 'شرکت سازنده', 'verbose_name_plural': 'شرکت سازنده'},
        ),
        migrations.AlterModelOptions(
            name='destinationcity',
            options={'verbose_name': 'شهر مقصد', 'verbose_name_plural': 'شهر مقصد'},
        ),
        migrations.AlterModelOptions(
            name='enginkind',
            options={'verbose_name': 'قدرت موتور', 'verbose_name_plural': 'قدرت موتور'},
        ),
        migrations.AlterModelOptions(
            name='origincity',
            options={'verbose_name': 'شهر مبدا', 'verbose_name_plural': 'شهر مبدا'},
        ),
        migrations.AlterModelOptions(
            name='pump',
            options={'verbose_name': 'پمپ', 'verbose_name_plural': 'پمپ'},
        ),
        migrations.AlterModelOptions(
            name='pumpmodel',
            options={'verbose_name': 'مدل پمپ', 'verbose_name_plural': 'مدل پمپ'},
        ),
        migrations.AlterField(
            model_name='buildercompany',
            name='name',
            field=models.CharField(max_length=300, verbose_name='اسم'),
        ),
        migrations.AlterField(
            model_name='destinationcity',
            name='name',
            field=models.CharField(max_length=200, verbose_name='اسم'),
        ),
        migrations.AlterField(
            model_name='enginkind',
            name='kind',
            field=models.CharField(max_length=50, verbose_name='نوع'),
        ),
        migrations.AlterField(
            model_name='origincity',
            name='name',
            field=models.CharField(max_length=150, verbose_name='اسم'),
        ),
        migrations.AlterField(
            model_name='pump',
            name='builder_company',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='builder_company', to='home.buildercompany', verbose_name='کمپانی سازنده'),
        ),
        migrations.AlterField(
            model_name='pump',
            name='code',
            field=models.IntegerField(verbose_name='کد'),
        ),
        migrations.AlterField(
            model_name='pump',
            name='courier',
            field=models.CharField(max_length=300, verbose_name='مامور تحویل'),
        ),
        migrations.AlterField(
            model_name='pump',
            name='date',
            field=models.DateField(verbose_name='تاریخ'),
        ),
        migrations.AlterField(
            model_name='pump',
            name='destination_city',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='destination_city', to='home.destinationcity', verbose_name='شهر مقصد'),
        ),
        migrations.AlterField(
            model_name='pump',
            name='engine_power',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pump', to='home.enginkind', verbose_name='قدرت موتور'),
        ),
        migrations.AlterField(
            model_name='pump',
            name='origin_city',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='origin_city', to='home.origincity', verbose_name='شهر مبدا'),
        ),
        migrations.AlterField(
            model_name='pump',
            name='pump_model',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pump', to='home.pumpmodel', verbose_name='مدل پمپ'),
        ),
        migrations.AlterField(
            model_name='pump',
            name='serial_number',
            field=models.IntegerField(verbose_name='شماره سریال'),
        ),
        migrations.AlterField(
            model_name='pumpmodel',
            name='model',
            field=models.CharField(max_length=100, verbose_name='مدل'),
        ),
    ]