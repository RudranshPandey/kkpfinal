# Generated by Django 3.2.19 on 2024-02-15 14:05

from django.db import migrations, models
import django.db.models.deletion
import shortuuid.main


class Migration(migrations.Migration):

    dependencies = [
        ('victims', '0046_alter_all_profiles_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_profiles',
            name='id',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, editable=False, max_length=22, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='VictimLifecycleEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_text', models.TextField()),
                ('attachment', models.FileField(blank=True, null=True, upload_to='attachments/')),
                ('entry_date', models.DateTimeField(auto_now_add=True)),
                ('victim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='victims.all_profiles')),
            ],
        ),
    ]
