# Generated by Django 3.2.7 on 2022-01-06 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    def initial_blotter_data(apps, schema_editor):
        from trading.models import Blotter, User
        
        u1 = User(name="John",email="John@bank1")
        u2 = User(name="Peter",email="Peter@bank1")
        u3 = User(name="Mark",email="Mark@bank2")
        
        u1.save()
        u2.save()
        u3.save()
        
        Blotter(ticker="PETR4", volume = 100, price=27.00, user=u1).save()
        Blotter(ticker="VALE3", volume = 150000, price=79, user=u1).save()
        Blotter(ticker="BOVA11", volume = 2022, price=97, user=u1).save()
        
        Blotter(ticker="AMER3", volume = 7240, price=27.00, user=u2).save()
        Blotter(ticker="ASAI3", volume = 1247, price=79, user=u2).save()
        Blotter(ticker="AZUL4", volume = 9999, price=97, user=u2).save()
        
        Blotter(ticker="B3SA3", volume = 1, price=27.00, user=u3).save()
        Blotter(ticker="BIDI11", volume = 2, price=79, user=u3).save()
        Blotter(ticker="BPAN4", volume = 3, price=97, user=u3).save()
        
        
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Blotter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=200)),
                ('volume', models.IntegerField()),
                ('price', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='trading.user')),
            ],
        ),
        migrations.RunPython(initial_blotter_data)
    ]