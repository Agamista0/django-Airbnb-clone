# Generated by Django 4.0.4 on 2022-05-10 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_footer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footer',
            name='description',
            field=models.TextField(max_length=2000),
        ),
    ]