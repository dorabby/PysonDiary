# Generated by Django 5.1.3 on 2024-11-17 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0003_anniversary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anniversary',
            name='anniv1',
            field=models.CharField(max_length=50, null=True, verbose_name='記念日1'),
        ),
        migrations.AlterField(
            model_name='anniversary',
            name='anniv2',
            field=models.CharField(max_length=50, null=True, verbose_name='記念日2'),
        ),
        migrations.AlterField(
            model_name='anniversary',
            name='anniv3',
            field=models.CharField(max_length=50, null=True, verbose_name='記念日3'),
        ),
        migrations.AlterField(
            model_name='anniversary',
            name='anniv4',
            field=models.CharField(max_length=50, null=True, verbose_name='記念日4'),
        ),
        migrations.AlterField(
            model_name='anniversary',
            name='anniv5',
            field=models.CharField(max_length=50, null=True, verbose_name='記念日5'),
        ),
    ]