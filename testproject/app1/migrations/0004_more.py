# Generated by Django 2.2.5 on 2019-12-03 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20191203_0246'),
    ]

    operations = [
        migrations.CreateModel(
            name='more',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
    ]