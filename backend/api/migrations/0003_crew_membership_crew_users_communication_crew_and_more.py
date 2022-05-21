# Generated by Django 4.0.4 on 2022-05-21 19:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_alter_communication_author_schema'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crew', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.crew')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'crew')},
            },
        ),
        migrations.AddField(
            model_name='crew',
            name='users',
            field=models.ManyToManyField(related_name='crews', through='api.Membership', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='communication',
            name='crew',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.crew'),
        ),
        migrations.AddField(
            model_name='schema',
            name='crew',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.crew'),
        ),
    ]
