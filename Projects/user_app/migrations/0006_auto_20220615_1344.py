# Generated by Django 3.0.1 on 2022-06-15 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0005_auto_20220615_1310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='messages',
        ),
        migrations.AddField(
            model_name='message',
            name='chat_room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='user_app.Chat'),
        ),
    ]
