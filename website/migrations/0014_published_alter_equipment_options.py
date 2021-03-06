# Generated by Django 4.0.1 on 2022-04-22 20:12

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_equipment_alter_trip_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Published',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Publicación')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='published/')),
            ],
            options={
                'verbose_name_plural': 'Publicaciones',
            },
        ),
        migrations.AlterModelOptions(
            name='equipment',
            options={'verbose_name_plural': 'Equipos'},
        ),
    ]
