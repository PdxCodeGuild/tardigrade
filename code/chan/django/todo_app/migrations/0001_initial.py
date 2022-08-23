# Generated by Django 4.0.4 on 2022-06-21 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('complete_date', models.DateField()),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]