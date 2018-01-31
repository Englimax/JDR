# Generated by Django 2.0 on 2018-01-31 12:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('DD35', '0004_chatroom_list_of_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='handle',
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='DD35.ChatRoom'),
        ),
    ]