# Generated by Django 3.0.8 on 2020-07-20 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RaidDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seed', models.IntegerField()),
                ('numDisks', models.IntegerField()),
                ('chunkSize', models.CharField(max_length=4)),
                ('numRequest', models.IntegerField()),
                ('reqSize', models.CharField(max_length=4)),
                ('workload', models.CharField(max_length=4)),
                ('writeFrac', models.IntegerField()),
                ('randRange', models.BigIntegerField()),
                ('level', models.IntegerField()),
                ('raid5', models.CharField(max_length=2)),
                ('reverse', models.BooleanField()),
                ('timing', models.BooleanField()),
                ('compute', models.BooleanField()),
                ('submitted', models.BooleanField()),
            ],
        ),
    ]
