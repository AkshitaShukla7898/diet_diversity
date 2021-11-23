# Generated by Django 3.1.5 on 2021-08-30 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SrNo', models.IntegerField(default=5)),
                ('Recipe_List', models.IntegerField(blank=True, default='Test', null=True)),
                ('Frequency_Day', models.IntegerField(default=1)),
                ('Frequency_Week', models.IntegerField(default=1)),
                ('Frequency_Month', models.IntegerField(default=2)),
                ('Amount', models.IntegerField(default=3)),
                ('Amount_Measure', models.IntegerField(default=4)),
                ('Consistency', models.IntegerField(blank=True, default='thick', null=True)),
                ('Remark', models.TextField(blank=True, default='Test', null=True)),
            ],
        ),
    ]
