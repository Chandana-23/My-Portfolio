# Generated by Django 4.0 on 2022-01-30 08:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0003_testimonial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='info',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
