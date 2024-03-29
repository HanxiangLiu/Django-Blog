# Generated by Django 4.1 on 2024-01-18 10:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("post", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("description", models.CharField(max_length=200)),
                ("thumbnail", models.URLField()),
                ("content", models.TextField()),
                ("content_html", models.TextField(blank=True, editable=False)),
                ("priority", models.IntegerField(default=-1)),
                ("is_hot", models.BooleanField(default=False)),
                (
                    "status",
                    models.PositiveIntegerField(
                        choices=[(1, "正常"), (0, "删除"), (2, "草稿")], default=2
                    ),
                ),
                ("publish_time", models.DateTimeField(auto_now_add=True)),
                ("time_id", models.CharField(blank=True, max_length=30)),
                ("read_num", models.PositiveIntegerField(default=0)),
                (
                    "author",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="post.category",
                    ),
                ),
            ],
            options={
                "ordering": ["-publish_time"],
            },
        ),
    ]
