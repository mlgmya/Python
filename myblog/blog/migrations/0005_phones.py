# Generated by Django 2.1.7 on 2019-04-15 08:36

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190415_1636'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mNo', models.CharField(max_length=32)),
                ('mMark', models.CharField(max_length=256)),
                ('mPrice', models.CharField(max_length=32)),
                ('mNote', models.CharField(max_length=1024)),
                ('mFile', models.CharField(max_length=256)),
            ],
        ),
    ]
