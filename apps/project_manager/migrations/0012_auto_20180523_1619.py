# Generated by Django 2.0.2 on 2018-05-23 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_manager', '0011_auto_20180523_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inceptionhostconfig',
            name='purpose',
            field=models.CharField(choices=[('0', '审核'), ('1', '查询')], default='0', max_length=2, verbose_name='用途'),
        ),
    ]