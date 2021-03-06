# Generated by Django 3.1.1 on 2021-03-14 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rms', '0010_auto_20210314_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitedata',
            name='dcenergy',
            field=models.FloatField(blank=True, help_text='Solar DC Energy in KWH', null=True),
        ),
        migrations.AlterField(
            model_name='sitedata',
            name='lpd',
            field=models.IntegerField(blank=True, help_text='Total LPD/Flow', null=True),
        ),
        migrations.AlterField(
            model_name='sitedata',
            name='prthrs',
            field=models.FloatField(blank=True, help_text='Pump Running Hrs', null=True),
        ),
        migrations.AlterField(
            model_name='sitedata',
            name='rmsId',
            field=models.CharField(blank=True, help_text='RMS ID or Site ID', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='sitedetails',
            name='capacity',
            field=models.CharField(blank=True, help_text='5HP AC or 3HP AC or other', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='sitedetails',
            name='cmcY',
            field=models.CharField(blank=True, help_text='Year of CMC', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sitedetails',
            name='location',
            field=models.CharField(blank=True, help_text='Village, Mandal', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sitedetails',
            name='regID',
            field=models.CharField(blank=True, help_text='If any registration ID is there', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='sitedetails',
            name='rmsId',
            field=models.CharField(blank=True, help_text='RMS ID or Site ID', max_length=40, null=True),
        ),
    ]
