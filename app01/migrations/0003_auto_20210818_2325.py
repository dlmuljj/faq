# Generated by Django 3.2 on 2021-08-18 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20210809_0908'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answers', models.TextField()),
                ('replier', models.CharField(max_length=32)),
                ('creator', models.CharField(max_length=32)),
                ('create_time', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Package',
            },
        ),
        migrations.CreateModel(
            name='SARADC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answers', models.TextField()),
                ('replier', models.CharField(max_length=32)),
                ('creator', models.CharField(max_length=32)),
                ('create_time', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'SARADC',
            },
        ),
        migrations.CreateModel(
            name='TVSensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answers', models.TextField()),
                ('replier', models.CharField(max_length=32)),
                ('creator', models.CharField(max_length=32)),
                ('create_time', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'TVSensor',
            },
        ),
        migrations.CreateModel(
            name='U2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answers', models.TextField()),
                ('replier', models.CharField(max_length=32)),
                ('creator', models.CharField(max_length=32)),
                ('create_time', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'U2',
            },
        ),
        migrations.CreateModel(
            name='U3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answers', models.TextField()),
                ('replier', models.CharField(max_length=32)),
                ('creator', models.CharField(max_length=32)),
                ('create_time', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'U3',
            },
        ),
        migrations.CreateModel(
            name='VDAC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answers', models.TextField()),
                ('replier', models.CharField(max_length=32)),
                ('creator', models.CharField(max_length=32)),
                ('create_time', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'VDAC',
            },
        ),
        migrations.RenameModel(
            old_name='Usb',
            new_name='MIPI',
        ),
        migrations.AlterModelOptions(
            name='ddr',
            options={'verbose_name_plural': 'DDR'},
        ),
        migrations.AlterModelOptions(
            name='dp',
            options={'verbose_name_plural': 'DP'},
        ),
        migrations.AlterModelOptions(
            name='hdmi',
            options={'verbose_name_plural': 'HDMI'},
        ),
        migrations.AlterModelOptions(
            name='mipi',
            options={'verbose_name_plural': 'MIPI'},
        ),
        migrations.AlterModelOptions(
            name='pll',
            options={'verbose_name_plural': 'PLL'},
        ),
        migrations.AlterModelOptions(
            name='serdes',
            options={'verbose_name_plural': 'Serdes'},
        ),
        migrations.AlterField(
            model_name='ddr',
            name='create_time',
            field=models.DateField(),
        ),
    ]