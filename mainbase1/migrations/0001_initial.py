# Generated by Django 3.2.9 on 2021-11-07 17:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mainbase1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_id', models.IntegerField(auto_created=True)),
                ('register_at', models.DateTimeField(auto_now_add=True)),
                ('pr_name', models.TextField()),
                ('pr_zacaz', models.TextField()),
                ('pr_proectir', models.TextField()),
                ('finished_at', models.DateTimeField(null=True)),
                ('is_finished', models.BooleanField(default=False)),
                ('estimated_finish_time', models.DateTimeField()),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mainbase1', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
