# Generated by Django 4.1.5 on 2023-01-31 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_count',
            field=models.CharField(default='0', max_length=1000),
        ),
    ]