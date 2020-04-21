# Generated by Django 2.2.3 on 2019-08-06 14:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import resturants.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resturants', '0003_auto_20190806_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='resturantlocation',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='resturantlocation',
            name='category',
            field=models.CharField(blank=True, max_length=120, null=True, validators=[resturants.validators.validate_resturant_category]),
        ),
    ]
