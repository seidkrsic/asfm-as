# Generated by Django 3.0.1 on 2022-06-10 10:24

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('subject', models.CharField(blank=True, default='No subject', max_length=200, null=True)),
                ('body', models.TextField()),
                ('is_read', models.BooleanField(default=False, null=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('recepient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messages', to='user_app.Profile')),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_app.Profile')),
            ],
            options={
                'ordering': ['is_read', '-created'],
            },
        ),
    ]
