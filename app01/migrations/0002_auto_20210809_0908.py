# Generated by Django 3.2.6 on 2021-08-09 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answers', models.TextField()),
                ('replier', models.CharField(max_length=32)),
                ('creator', models.CharField(max_length=32)),
                ('create_time', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Hdmi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answers', models.TextField()),
                ('replier', models.CharField(max_length=32)),
                ('creator', models.CharField(max_length=32)),
                ('create_time', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Pll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answers', models.TextField()),
                ('replier', models.CharField(max_length=32)),
                ('creator', models.CharField(max_length=32)),
                ('create_time', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Serdes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answers', models.TextField()),
                ('replier', models.CharField(max_length=32)),
                ('creator', models.CharField(max_length=32)),
                ('create_time', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Usb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answers', models.TextField()),
                ('replier', models.CharField(max_length=32)),
                ('creator', models.CharField(max_length=32)),
                ('create_time', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='ddr',
            name='create_time',
            field=models.DateField(auto_now=True),
        ),
    ]