# Generated by Django 2.2.6 on 2019-11-01 03:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(default='', max_length=100, verbose_name='province')),
                ('city', models.CharField(default='', max_length=100, verbose_name='city')),
                ('district', models.CharField(default='', max_length=100, verbose_name='district')),
                ('address', models.CharField(default='', max_length=100, verbose_name='address')),
                ('signer_name', models.CharField(default='', max_length=100, verbose_name='signer_name')),
                ('signer_mobile', models.CharField(default='', max_length=11, verbose_name='signer_mobile')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add_time')),
            ],
            options={
                'verbose_name': 'UserAddress',
                'verbose_name_plural': 'UserAddress',
            },
        ),
        migrations.CreateModel(
            name='UserFav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add_time')),
            ],
            options={
                'verbose_name': 'UserFav',
                'verbose_name_plural': 'UserFav',
            },
        ),
        migrations.CreateModel(
            name='UserLeavingMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_type', models.IntegerField(choices=[(1, 'Leave message'), (2, 'complain'), (3, 'ask for help'), (4, 'service'), (5, 'ask for goods')], default=1, help_text='MESSAGE CHOICES: 1(Leave message),2(complain),3(ask for help),4(service),5(ask for goods)', verbose_name='message_type')),
                ('subject', models.CharField(default='', max_length=100, verbose_name='subject')),
                ('message', models.TextField(default='', help_text='message context', verbose_name='message')),
                ('file', models.FileField(help_text='file', upload_to='message/images/', verbose_name='file')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add_time')),
            ],
            options={
                'verbose_name': 'UserLeavingMessage',
                'verbose_name_plural': 'UserLeavingMessage',
            },
        ),
    ]
