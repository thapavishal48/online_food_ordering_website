# Generated by Django 3.0.2 on 2020-01-24 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fooditem', '0004_fooditem_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='group',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
