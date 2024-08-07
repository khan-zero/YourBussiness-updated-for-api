# Generated by Django 5.0.7 on 2024-08-04 10:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BusnesApp', '0005_whyus_whyusqa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255)),
                ('Sub_Title', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='media/Skills')),
            ],
        ),
        migrations.AlterModelOptions(
            name='whyus',
            options={'verbose_name': 'WhyUS', 'verbose_name_plural': 'WhyUS'},
        ),
        migrations.AlterModelOptions(
            name='whyusqa',
            options={'verbose_name': 'WhyUsQA', 'verbose_name_plural': 'WhyUsQA'},
        ),
        migrations.AddField(
            model_name='whyusqa',
            name='why_us',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='BusnesApp.whyus'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='SkillsUsage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('usage', models.IntegerField()),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BusnesApp.skills')),
            ],
        ),
    ]