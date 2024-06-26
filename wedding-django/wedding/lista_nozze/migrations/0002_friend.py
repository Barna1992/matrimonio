# Generated by Django 4.2.9 on 2024-01-05 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lista_nozze', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=50)),
                ('comment', models.TextField()),
                ('item_titles', models.CharField(max_length=255)),
                ('item_price', models.FloatField()),
            ],
        ),
    ]
