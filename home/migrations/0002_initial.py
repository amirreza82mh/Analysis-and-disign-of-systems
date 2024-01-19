# Generated by Django 4.2.6 on 2024-01-18 14:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sanse_viewer',
            name='viewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sans',
            name='exhibition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.exhibition'),
        ),
        migrations.AddField(
            model_name='artwork_exhibition_curator',
            name='artwork',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.artwork'),
        ),
        migrations.AddField(
            model_name='artwork_exhibition_curator',
            name='curator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='artwork_exhibition_curator',
            name='exhibition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.exhibition'),
        ),
        migrations.AddField(
            model_name='artwork',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='sanse_viewer',
            unique_together={('ticket', 'sanse', 'viewer')},
        ),
        migrations.AlterUniqueTogether(
            name='sans',
            unique_together={('exhibition', 'start_time', 'finish_time')},
        ),
        migrations.AlterUniqueTogether(
            name='artwork_exhibition_curator',
            unique_together={('exhibition', 'artwork', 'curator')},
        ),
    ]
