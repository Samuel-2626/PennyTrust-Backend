# Generated by Django 3.1.5 on 2021-01-20 14:13

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, null=True)),
                ('last_name', models.CharField(max_length=255, null=True)),
                ('title', models.CharField(choices=[('mr', 'Mr'), ('mrs', 'Mrs'), ('alhaji', 'Alhaji'), ('chief', 'Chief'), ('dr', 'Dr')], max_length=20)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('date_of_birth', models.DateField()),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=15)),
                ('state', models.CharField(choices=[('abia', 'Abia'), ('adamawa', 'Adamawa'), ('akwaibom', 'Akwa Ibom'), ('anambra', 'Anambra'), ('bauchi', 'Bauchi'), ('bayelsa', 'Bayelsa'), ('benue', 'Benue'), ('borno', 'Borno'), ('crossriver', 'Cross River'), ('delta', 'Delta'), ('ebonyi', 'Ebonyi'), ('edo', 'Edo'), ('ekiti', 'Ekiti'), ('enugu', 'Enugu'), ('gombe', 'Gombe'), ('imo', 'Imo'), ('jigawa', 'Jigawa'), ('kaduna', 'Kaduna'), ('kano', 'Kano'), ('katsina', 'Katsina'), ('kebbi', 'Kebbi'), ('kogi', 'Kogi'), ('kwara', 'Kwara'), ('lagos', 'Lagos'), ('nasarawa', 'Nasawara'), ('niger', 'Niger'), ('ogun', 'Ogun'), ('ondo', 'Ondo'), ('osun', 'Osun'), ('oyo', 'Oyo'), ('plateau', 'Plateau'), ('rivers', 'Rivers'), ('sokoto', 'Sokoto'), ('taraba', 'Taraba'), ('yobe', 'Yobe'), ('zamfara', 'Zamfara')], max_length=10)),
                ('place_of_work', models.CharField(max_length=20)),
                ('ippis_number', models.CharField(max_length=20)),
                ('salary_bank_name', models.CharField(choices=[('access', 'Access Bank Plc'), ('citi', 'Citibank Nigeria Limited'), ('eco', 'Ecobank Nigeria Plc'), ('fidelity', 'Fidelity Banl Plc'), ('monument', 'First City Monument Bank Limited'), ('first', 'First Bank of Nigeria Limited'), ('guaranty', 'Guaranty Trust Bank Plc'), ('keystone', 'Keystone Bank Limited'), ('polaris', 'Polaris Bank Limited'), ('stanbic', 'Stanbic IBTC Bank Plc'), ('standard', 'Standard Chartered'), ('sterling', 'Sterling Bank Plc'), ('titan', 'Titan Trust Bank Limited'), ('union', 'Union Bank of Nigeria Plc'), ('united', 'United Bank for Afria Plc'), ('unity', 'Unity Bank Plc'), ('wema', 'Wema Bank Plc'), ('zenith', 'Zenith Bank Plc')], max_length=20)),
                ('account_number', models.PositiveSmallIntegerField()),
                ('loan_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tenor', models.CharField(choices=[('2', '2 Months'), ('3', '3 Months'), ('4', '4 Months'), ('5', '5 Months'), ('6', '6 Months'), ('7', '7 Months'), ('8', '8 Months'), ('9', '9 Months'), ('10', '10 Months'), ('11', '11 Months'), ('12', '12 Months'), ('13', '13 Months'), ('14', '14 Months'), ('15', '15 Months'), ('16', '16 Months'), ('17', '17 Months'), ('18', '18 Months')], max_length=10)),
                ('referral_code', models.CharField(blank=True, max_length=20, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='my_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]