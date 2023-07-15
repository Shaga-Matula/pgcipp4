# Generated by Django 3.2.20 on 2023-07-15 18:24

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Lvl',
            fields=[
                ('Level_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('kyu_level', models.CharField(max_length=50)),
                ('belt_color', models.CharField(max_length=50)),
                ('kata_name', models.CharField(max_length=50)),
                ('kata_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('syllabus_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
            ],
            options={
                'ordering': ['-kyu_level'],
            },
        ),
        migrations.CreateModel(
            name='Student_info',
            fields=[
                ('Student_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('Date_of_birth', models.DateField()),
                ('Email', models.EmailField(max_length=50)),
                ('Address_1', models.CharField(max_length=50)),
                ('Address_2', models.CharField(max_length=50, null=True)),
                ('Post_code', models.CharField(max_length=10)),
                ('Content', models.TextField()),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('Student_Grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shotokanapp.student_lvl')),
            ],
            options={
                'ordering': ['-Student_ID'],
            },
        ),
    ]