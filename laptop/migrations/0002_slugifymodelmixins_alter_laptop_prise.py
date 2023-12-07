# Generated by Django 4.2.7 on 2023-12-02 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlugifyModelMixins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='laptop',
            name='prise',
            field=models.IntegerField(),
        ),
    ]
