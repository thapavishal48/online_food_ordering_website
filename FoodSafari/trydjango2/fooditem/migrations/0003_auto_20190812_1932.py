# Generated by Django 2.2.3 on 2019-08-12 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fooditem', '0002_fooditem_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_image'),
        ),
    ]
