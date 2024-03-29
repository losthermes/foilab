# Generated by Django 2.2.2 on 2019-07-28 00:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LAB', '0005_auto_20190726_1108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fuel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample_id', models.CharField(blank=True, max_length=200, null=True)),
                ('package', models.CharField(blank=True, max_length=200, null=True)),
                ('Fuel', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SampleTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('result', models.CharField(blank=True, max_length=200, null=True)),
                ('sample', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LAB.Sample')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='First_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='Last_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='adress',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='city',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='company',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='state',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='status_note',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='zipcode',
        ),
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sample',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LAB.Customer'),
        ),
        migrations.AddField(
            model_name='package',
            name='tests',
            field=models.ManyToManyField(blank=True, to='LAB.Test'),
        ),
    ]
