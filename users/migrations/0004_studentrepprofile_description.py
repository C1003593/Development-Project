# Generated by Django 4.2 on 2024-03-02 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_mentorprofile_description_alter_mentorprofile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentrepprofile',
            name='Description',
            field=models.TextField(null=True),
        ),
    ]