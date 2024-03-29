# Generated by Django 4.0.4 on 2022-05-22 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0009_rename_cv_about'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': 'about', 'verbose_name_plural': 'abouts'},
        ),
        migrations.RenameField(
            model_name='about',
            old_name='description',
            new_name='description1',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='title',
            new_name='title1',
        ),
        migrations.AddField(
            model_name='about',
            name='description2',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='description3',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='description4',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='title2',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='title3',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='title4',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(upload_to='about'),
        ),
    ]
