# Generated by Django 4.2.5 on 2023-10-04 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('v_to_a_converter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.FileField(blank=True, null=True, upload_to='media', verbose_name='Media')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
