# Generated by Django 5.2 on 2025-07-26 10:04

import education.models
import education.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('symptoms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True)),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('summary', models.CharField(blank=True, help_text='Short preview text (max 150 chars)', max_length=150)),
                ('content', models.TextField()),
                ('tags', models.JSONField(blank=True, default=education.models.Article.default_tags, help_text="List of tag strings, e.g., ['tag1', 'tag2']", validators=[education.validators.validate_string_list])),
                ('cover_image', models.URLField(blank=True, help_text='URL to cover image (16:9 aspect ratio recommended)', validators=[education.validators.validate_image_url])),
                ('related_conditions', models.ManyToManyField(blank=True, to='symptoms.condition')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True)),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('video_url', models.URLField(blank=True, help_text='URL to the video (can be YouTube, Vimeo, or any other video platform)', null=True, validators=[education.validators.validate_video_url])),
                ('youtube_url', models.URLField(blank=True, help_text='Legacy field - will be removed', null=True)),
                ('duration_minutes', models.PositiveSmallIntegerField(help_text='Duration in minutes (max 600 minutes / 10 hours)', validators=[education.validators.validate_duration_minutes])),
                ('related_symptoms', models.ManyToManyField(blank=True, to='symptoms.symptom')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
