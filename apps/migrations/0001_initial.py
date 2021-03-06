# Generated by Django 4.0.4 on 2022-04-20 19:39

import apps.common.types
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('release_year', models.IntegerField(choices=[(1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], default=2022, verbose_name='year')),
                ('drive', models.CharField(choices=[('Front-wheel', 'F'), ('Rear-wheel', 'B'), ('All-wheel', 'Full')], help_text='Front-wheel - F\nRear-wheel - B\nAll-wheel - Full', max_length=255)),
                ('transmission', models.CharField(choices=[('Atomatic', 'A'), ('Manual', 'M')], help_text='Atomatic - A\nManual - M', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CarPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(choices=[('USD', 'USD'), ('BYN', 'BYN'), ('RUB', 'RUB')], default=apps.common.types.CurrencyType['USD'], max_length=6)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('count', models.PositiveSmallIntegerField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='price', to='apps.car')),
            ],
        ),
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('car_prices', models.ManyToManyField(to='apps.carprice')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(choices=[('USD', 'USD'), ('BYN', 'BYN'), ('RUB', 'RUB')], default=apps.common.types.CurrencyType['USD'], max_length=6)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('currency', models.CharField(choices=[('USD', 'USD'), ('BYN', 'BYN'), ('RUB', 'RUB')], default=apps.common.types.CurrencyType['USD'], max_length=6)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='offer', to='apps.car')),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='offer', to='apps.dealer')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='offer', to='apps.profile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DealerAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.CharField(help_text='Building number or name', max_length=300)),
                ('street', models.CharField(max_length=300)),
                ('area', models.CharField(help_text='Area, state, province', max_length=300)),
                ('city', models.CharField(max_length=200)),
                ('country', models.CharField(help_text='ISO2 country code', max_length=2)),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dealer_address', to='apps.dealer')),
            ],
        ),
    ]
