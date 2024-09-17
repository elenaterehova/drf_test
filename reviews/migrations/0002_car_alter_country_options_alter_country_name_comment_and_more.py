# Generated by Django 5.1.1 on 2024-09-15 12:34

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название автомобиля', max_length=254)),
                ('year_of_release', models.DateField()),
                ('year_of_completion', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Cars',
            },
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Countries'},
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(help_text='Название страны', max_length=254),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_email', models.EmailField(max_length=254)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment', models.TextField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.car')),
            ],
            options={
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название производителя.', max_length=254)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.country')),
            ],
            options={
                'verbose_name_plural': 'Manufacturers',
            },
        ),
        migrations.AddField(
            model_name='car',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.manufacturer'),
        ),
    ]
