# Generated by Django 2.2.2 on 2019-07-22 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='personel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AD_SOYAD', models.CharField(max_length=100)),
                ('DEPARTMAN', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='donanım_dbs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TUR', models.CharField(max_length=100)),
                ('MARKA', models.CharField(max_length=100)),
                ('MODEL', models.CharField(max_length=100)),
                ('SERI_NO', models.CharField(max_length=100)),
                ('LOKASYON', models.CharField(max_length=100)),
                ('DURUM', models.BooleanField(default=True)),
                ('EVENT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_page.personel')),
            ],
        ),
    ]