# Generated by Django 4.0.4 on 2022-05-21 20:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_crew_membership_crew_users_communication_crew_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='communication',
            options={'ordering': ['datetime_created']},
        ),
        migrations.AlterModelOptions(
            name='schema',
            options={'ordering': ['datetime_created']},
        ),
        migrations.AddField(
            model_name='communication',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schema',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
