# Generated by Django 5.0 on 2023-12-22 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock_List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(default='', max_length=30)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
