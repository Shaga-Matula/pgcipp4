# Generated by Django 3.2.20 on 2023-07-16 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shotokanapp', '0004_auto_20230716_2157'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student_info',
            options={'ordering': ['-last_name']},
        ),
    ]
