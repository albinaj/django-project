# Generated by Django 3.0 on 2020-01-06 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_faculty'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stdid', models.IntegerField(default=0, unique=True)),
                ('admno', models.IntegerField(default=0, unique=True)),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=30)),
                ('dob', models.DateField(max_length=10)),
                ('gender', models.CharField(max_length=20)),
                ('mobile', models.IntegerField(default=0)),
                ('admdate', models.DateField(max_length=20)),
                ('gaurdian', models.CharField(max_length=20)),
                ('batch', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
