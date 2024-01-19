# Generated by Django 4.2.6 on 2024-01-18 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('artwork_id', models.AutoField(primary_key=True, serialize=False)),
                ('artwork_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('rating', models.PositiveIntegerField(choices=[(0, 'Not Rated'), (1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')], default=0)),
                ('picture', models.ImageField(upload_to='home/picture/')),
                ('creation_time', models.TimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Artwork_Exhibition_Curator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Exhibition',
            fields=[
                ('exhibition_id', models.AutoField(primary_key=True, serialize=False)),
                ('exhibition_name', models.CharField(max_length=100)),
                ('capacity', models.IntegerField(default=20)),
                ('exhibition_place', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('picture', models.ImageField(upload_to='home/picture')),
                ('start_date', models.DateField()),
                ('finish_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Sans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('finish_time', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Sanse_Viewer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket', models.CharField(max_length=255)),
                ('sanse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.sans')),
            ],
        ),
    ]
