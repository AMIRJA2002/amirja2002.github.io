# Generated by Django 5.0 on 2023-12-27 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_buildercompany_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pump',
            name='status',
            field=models.CharField(choices=[('در حال تعمیر', 'در حال تعمیر'), ('تعمیر شده', 'تعمیر شده')], default='تعمیر شده', max_length=20),
        ),
    ]