# Generated by Django 4.2.9 on 2024-03-11 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lista_nozze', '0002_friend'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('travel', 'travel'), ('home', 'home')], default='travel', max_length=20),
        ),
    ]
