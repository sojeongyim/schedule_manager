# Generated by Django 2.0.4 on 2018-04-30 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miso', '0002_auto_20180430_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='time',
            field=models.CharField(choices=[('D', '오픈'), ('D1', '준오픈'), ('M', '미들'), ('M1', '늦미들'), ('N', '마감')], max_length=5),
        ),
    ]