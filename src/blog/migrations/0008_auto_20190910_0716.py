# Generated by Django 2.2.5 on 2019-09-10 07:16

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190910_0652'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='blogpost',
            managers=[
                ('objecsts', django.db.models.manager.Manager()),
            ],
        ),
    ]
