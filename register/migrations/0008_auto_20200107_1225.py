# Generated by Django 3.0 on 2020-01-07 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0007_remove_student_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='admnno',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='stdid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
