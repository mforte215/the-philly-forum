# Generated by Django 4.0.4 on 2022-05-24 12:04

from django.db import migrations, models
import tinymce.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=400)),
                ('header_image_url', models.URLField()),
                ('published_date', models.DateField(auto_now_add=True)),
                ('draft', models.BooleanField(default=True)),
                ('top_post', models.BooleanField(default=False)),
                ('content', tinymce.models.HTMLField()),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
            ],
        ),
    ]