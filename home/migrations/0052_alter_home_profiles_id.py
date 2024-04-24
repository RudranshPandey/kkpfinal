# Generated by Django 3.2.19 on 2024-04-24 14:13

from django.db import migrations, models
import shortuuid.main


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0051_alter_home_profiles_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home_profiles',
            name='id',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, editable=False, max_length=22, primary_key=True, serialize=False),
        ),
    ]
