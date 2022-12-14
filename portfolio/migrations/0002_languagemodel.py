# Generated by Django 4.1 on 2022-08-27 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LanguageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=255, verbose_name='Language')),
                ('listening', models.PositiveIntegerField(verbose_name='Listening')),
                ('Speaking', models.PositiveIntegerField(verbose_name='Speaking')),
                ('Reading', models.PositiveIntegerField(verbose_name='Reading')),
                ('Writing', models.PositiveIntegerField(verbose_name='Writing')),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
            },
        ),
    ]
