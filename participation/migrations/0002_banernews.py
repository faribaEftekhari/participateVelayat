# Generated by Django 3.2.5 on 2021-12-10 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='banernews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='1.jpg', null=True, upload_to='ImageSlider/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
