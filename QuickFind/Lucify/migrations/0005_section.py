# Generated by Django 4.2.5 on 2024-12-10 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lucify', '0004_deliveries'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('feature1', models.TextField()),
                ('feature2', models.TextField()),
                ('feature3', models.TextField()),
                ('more', models.TextField()),
                ('img', models.ImageField(upload_to='sections/')),
            ],
        ),
    ]
