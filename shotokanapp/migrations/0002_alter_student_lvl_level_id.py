# Generated by Django 3.2.20 on 2023-07-15 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shotokanapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_lvl',
            name='Level_ID',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
