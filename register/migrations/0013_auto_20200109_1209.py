# Generated by Django 3.0 on 2020-01-09 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0012_auto_20200109_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmark',
            name='assessmentno',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentmark',
            name='percentage',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentmark',
            name='sub1mark',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentmark',
            name='sub2mark',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentmark',
            name='sub3mark',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
