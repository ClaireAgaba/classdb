# Generated by Django 4.2.7 on 2023-11-23 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movielib', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rental',
            old_name='branch_number',
            new_name='branch',
        ),
        migrations.RenameField(
            model_name='rental',
            old_name='video_number',
            new_name='video',
        ),
        migrations.RemoveField(
            model_name='rental',
            name='title',
        ),
        migrations.AddField(
            model_name='rental',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
