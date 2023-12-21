# Generated by Django 4.2.6 on 2023-12-08 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FirstName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='LastName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Patronymic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house', models.CharField(max_length=10)),
                ('building', models.CharField(max_length=10)),
                ('apartment', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=15)),
                ('first_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phonebook.firstname')),
                ('last_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phonebook.lastname')),
                ('patronymic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phonebook.patronymic')),
                ('street', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phonebook.street')),
            ],
        ),
    ]