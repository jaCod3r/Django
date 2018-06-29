# Generated by Django 2.0.6 on 2018-06-25 22:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('location_folder', models.FilePathField(allow_folders=True)),
            ],
        ),
    ]
