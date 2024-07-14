# Generated by Django 5.0 on 2024-07-13 19:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_chat', '0002_ch_author_to_fk'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groupmessage',
            old_name='message',
            new_name='content',
        ),
        migrations.AlterField(
            model_name='groupmessage',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='a_chat.chatgroup'),
        ),
    ]
