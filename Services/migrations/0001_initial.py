# Generated by Django 4.0.3 on 2022-04-15 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClassNbr', models.IntegerField()),
                ('CourseCode', models.CharField(max_length=95)),
                ('CourseTitle', models.CharField(max_length=95)),
                ('CourseType', models.CharField(max_length=95)),
                ('CourseSystem', models.CharField(max_length=95)),
                ('Faculty', models.CharField(max_length=95)),
                ('Slot', models.CharField(max_length=95)),
                ('CourseMode', models.CharField(max_length=95)),
            ],
        ),
    ]
