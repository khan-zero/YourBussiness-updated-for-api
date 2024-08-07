# Generated by Django 5.0.7 on 2024-08-04 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BusnesApp', '0014_footerliks'),
    ]

    operations = [
        migrations.CreateModel(
            name='BeginPageContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_earnings', models.IntegerField()),
                ('a_earnings', models.IntegerField()),
                ('tasks', models.IntegerField()),
                ('pending_requests', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DevelopmentApproach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('conclusion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Illustrations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('body', models.TextField()),
                ('author', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activities', models.CharField(max_length=255)),
                ('percentage', models.IntegerField()),
            ],
        ),
    ]
