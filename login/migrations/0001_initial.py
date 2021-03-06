# Generated by Django 4.0.4 on 2022-05-13 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=15, null=True, verbose_name='Categry')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Book')),
                ('author', models.CharField(blank=True, max_length=25, null=True, verbose_name='Author')),
                ('date_publish', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date')),
                ('price', models.SmallIntegerField(blank=True, null=True, verbose_name='Price')),
                ('quantity', models.SmallIntegerField(blank=True, null=True, verbose_name='Quantity')),
                ('publication', models.CharField(blank=True, max_length=50, null=True, verbose_name='Publication')),
                ('description', models.TextField()),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book', to='login.category', verbose_name='Category')),
            ],
        ),
    ]
