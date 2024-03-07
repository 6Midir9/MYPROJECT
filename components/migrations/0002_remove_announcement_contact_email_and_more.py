# Generated by Django 5.0.3 on 2024-03-07 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='contact_email',
        ),
        migrations.RemoveField(
            model_name='announcement',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='announcement',
            name='description',
        ),
        migrations.RemoveField(
            model_name='announcement',
            name='price',
        ),
        migrations.AddField(
            model_name='announcement',
            name='text',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]