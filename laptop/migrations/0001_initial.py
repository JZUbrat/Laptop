# Generated by Django 4.2.7 on 2023-11-28 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=2000)),
                ('prise', models.ImageField(upload_to='')),
                ('image', models.ImageField(default='img/lenovo_legion_pro_5_Gen_8.jpg', upload_to='img')),
                ('description', models.TextField()),
            ],
        ),
    ]
