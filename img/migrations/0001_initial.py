# Generated by Django 4.0.4 on 2022-05-16 00:47

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProfilePic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profileusername', models.CharField(max_length=1000)),
                ('imagelink', models.CharField(max_length=1000)),
                ('username', models.CharField(max_length=1000)),
            ],
            managers=[
                ('objecs', django.db.models.manager.Manager()),
            ],
        ),
    ]