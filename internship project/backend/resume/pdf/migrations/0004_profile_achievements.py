# Generated by Django 4.1 on 2022-09-28 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0003_rename_skills_profile_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='achievements',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
