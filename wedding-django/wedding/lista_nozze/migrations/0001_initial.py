# Generated by Django 4.2.8 on 2023-12-31 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('picture', models.ImageField(blank=True, null=True, upload_to='pictures/')),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
