# Generated by Django 5.0.8 on 2024-10-16 06:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0067_alter_agent_style_icon"),
    ]

    operations = [
        migrations.CreateModel(
            name="WebScraper",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(blank=True, default=None, max_length=200, null=True, unique=True)),
                (
                    "type",
                    models.CharField(
                        choices=[("firecrawl", "Firecrawl"), ("olostep", "Olostep"), ("jina", "Jina")],
                        default="jina",
                        max_length=20,
                    ),
                ),
                ("api_key", models.CharField(blank=True, default=None, max_length=200, null=True)),
                ("api_url", models.URLField(blank=True, default=None, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="serverchatsettings",
            name="web_scraper",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="web_scraper",
                to="database.webscraper",
            ),
        ),
    ]
