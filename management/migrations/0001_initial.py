# Generated by Django 4.1 on 2022-08-18 15:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=150)),
                ('phone_number', models.IntegerField()),
                ('index', models.IntegerField(blank=True, null=True)),
                ('pay_type', models.CharField(max_length=20)),
                ('coupon', models.CharField(blank=True, max_length=20)),
                ('products', models.JSONField()),
                ('confirm', models.BooleanField(blank=True, default=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('delivered', models.BooleanField(blank=True, default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
