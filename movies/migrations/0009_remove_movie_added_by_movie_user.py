# Generated by Django 4.2 on 2023-04-18 14:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0008_movieorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='added_by',
        ),
        migrations.AddField(
            model_name='movie',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='movies', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
