# Generated by Django 3.2.18 on 2023-03-24 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=90)),
                ('password', models.CharField(max_length=90)),
                ('type', models.CharField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='resorts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phonenumber', models.BigIntegerField()),
                ('email', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('pin', models.IntegerField()),
                ('district', models.CharField(max_length=50)),
                ('license', models.BigIntegerField()),
                ('lattitude', models.CharField(max_length=1000)),
                ('longitude', models.CharField(max_length=1000)),
                ('lid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_planning.login')),
            ],
        ),
        migrations.CreateModel(
            name='restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phonenumber', models.BigIntegerField()),
                ('email', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('pin', models.IntegerField()),
                ('district', models.CharField(max_length=50)),
                ('license', models.BigIntegerField()),
                ('lattitude', models.CharField(max_length=1000)),
                ('longitude', models.CharField(max_length=1000)),
                ('lid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_planning.login')),
            ],
        ),
        migrations.CreateModel(
            name='touristplace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('latitude', models.CharField(max_length=50)),
                ('longitude', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='userregistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=60)),
                ('gender', models.CharField(max_length=50)),
                ('phonenumber', models.BigIntegerField()),
                ('email', models.CharField(max_length=50)),
                ('lid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_planning.login')),
            ],
        ),
        migrations.CreateModel(
            name='touristplacereviewrating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=60)),
                ('rating', models.FloatField()),
                ('date', models.DateField()),
                ('tpid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_planning.resorts')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_planning.userregistration')),
            ],
        ),
        migrations.CreateModel(
            name='restaurantreviewrating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=60)),
                ('rating', models.FloatField()),
                ('date', models.DateField()),
                ('restaurantid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_planning.restaurant')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_planning.userregistration')),
            ],
        ),
        migrations.CreateModel(
            name='restaurantfacility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facility', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=70)),
                ('image', models.ImageField(upload_to='')),
                ('restaurantid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_planning.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='resortroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomno', models.IntegerField()),
                ('type', models.CharField(max_length=20)),
                ('image', models.FileField(upload_to='')),
                ('amount', models.FloatField()),
                ('resortid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_planning.resorts')),
            ],
        ),
        migrations.CreateModel(
            name='resortreviewrating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=60)),
                ('rating', models.FloatField()),
                ('date', models.DateField()),
                ('resortid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_planning.resorts')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_planning.userregistration')),
            ],
        ),
        migrations.CreateModel(
            name='resortfacility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facility', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=70)),
                ('image', models.ImageField(upload_to='')),
                ('resortid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_planning.resorts')),
            ],
        ),
        migrations.CreateModel(
            name='fooditem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=90)),
                ('foodname', models.CharField(max_length=60)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.CharField(max_length=60)),
                ('price', models.FloatField()),
                ('restaurantid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_planning.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('reply', models.CharField(max_length=90)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_planning.userregistration')),
            ],
        ),
    ]
