# Generated by Django 5.0.4 on 2024-05-02 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='auth_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.DecimalField(decimal_places=10, max_digits=10)),
            ],
        ),
    ]
