# Generated by Django 2.0.4 on 2018-04-30 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miso', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='day',
            field=models.CharField(choices=[('월요일', '월요일'), ('화요일', '화요일'), ('수요일', '수요일'), ('목요일', '목요일'), ('금요일', '금요일'), ('토요일', '토요일'), ('일요일', '일요일')], max_length=10),
        ),
        migrations.AlterField(
            model_name='day',
            name='time',
            field=models.IntegerField(choices=[('D', '오픈'), ('D1', '준오픈'), ('M', '미들'), ('M1', '늦미들'), ('N', '마감')], max_length=5),
        ),
    ]
