# Generated by Django 3.2.5 on 2021-12-18 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participation', '0006_auto_20211216_2225'),
    ]

    operations = [
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.TextField(blank=True, default=' ')),
            ],
        ),
        migrations.AddField(
            model_name='volenteer',
            name='field',
            field=models.CharField(default=' ', max_length=300),
        ),
    ]
