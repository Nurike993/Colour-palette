# Generated by Django 4.2.2 on 2024-04-07 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_color_palette_alter_color_hex_code_alter_color_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Palette',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('color1', models.CharField(max_length=100, null=True)),
                ('hex_code1', models.CharField(max_length=7, null=True)),
                ('color2', models.CharField(max_length=100, null=True)),
                ('hex_code2', models.CharField(max_length=7, null=True)),
                ('color3', models.CharField(max_length=100, null=True)),
                ('hex_code3', models.CharField(max_length=7, null=True)),
                ('color4', models.CharField(max_length=100, null=True)),
                ('hex_code4', models.CharField(max_length=7, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Color',
        ),
    ]