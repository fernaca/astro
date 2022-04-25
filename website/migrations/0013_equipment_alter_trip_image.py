# Generated by Django 4.0.1 on 2022-04-22 19:09

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_alter_trip_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='equipment/')),
            ],
            options={
                'verbose_name_plural': 'Equipments',
            },
        ),
        migrations.AlterField(
            model_name='trip',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='trips/'),
        ),
    ]