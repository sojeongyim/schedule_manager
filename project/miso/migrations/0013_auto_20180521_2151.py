# Generated by Django 2.0.4 on 2018-05-21 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miso', '0012_auto_20180521_0947'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='still_possible_schedule',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='still_possible_schedule',
            name='day_id',
        ),
        migrations.RemoveField(
            model_name='still_possible_schedule',
            name='staff_id',
        ),
        migrations.AddField(
            model_name='possible_schedule',
            name='is_assigned',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='day',
            name='time',
            field=models.CharField(choices=[('D', '선오픈'), ('D1', '후오픈'), ('D2', '준오픈'), ('M', '선미들'), ('M1', '미들1'), ('M2', '미들2'), ('M3', '미들3'), ('M4', '늦미들'), ('N', '선마감'), ('N1', '마감'), ('N2', '후마감')], max_length=5),
        ),
        migrations.DeleteModel(
            name='Still_possible_schedule',
        ),
    ]