# Generated by Django 3.2.3 on 2021-05-13 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=65536)),
                ('template_url', models.CharField(max_length=65536)),
            ],
        ),
    ]
