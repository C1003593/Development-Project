# Generated by Django 4.2.3 on 2024-04-13 00:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0002_remove_message_id_message_message_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]