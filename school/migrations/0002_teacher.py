# Generated by Django 4.0.4 on 2022-04-19 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('emp_roll', models.IntegerField(unique=True)),
                ('city', models.CharField(max_length=70)),
                ('salary', models.IntegerField()),
                ('join_date', models.DateField()),
            ],
        ),
    ]
