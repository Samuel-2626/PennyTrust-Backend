from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):

  STATUS_TENOR = (
    ('2', '2 Months'),
    ('3', '3 Months'),
    ('4', '4 Months'),
    ('5', '5 Months'),
    ('6', '6 Months'),
    ('7', '7 Months'),
    ('8', '8 Months'),
    ('9', '9 Months'),
    ('10', '10 Months'),
    ('11', '11 Months'),
    ('12', '12 Months'),
    ('13', '13 Months'),
    ('14', '14 Months'),
    ('15', '15 Months'),
    ('16', '16 Months'),
    ('17', '17 Months'),
    ('18', '18 Months'),
    
  )

  STATUS_TITLE = (
    ('mr', 'Mr'),
    ('mrs', 'Mrs'),
    ('alhaji', 'Alhaji'),
    ('chief', 'Chief'),
    ('dr', 'Dr'),
  )

  STATUS_GENDER = (
    ('male', 'Male'),
    ('female', 'Female'),
  )

  STATUS_STATE = (
    ('abia', 'Abia'),
    ('adamawa', 'Adamawa'),
    ('akwaibom', 'Akwa Ibom'),
    ('anambra', 'Anambra'),
    ('bauchi', 'Bauchi'),
    ('bayelsa', 'Bayelsa'),
    ('benue', 'Benue'),
    ('borno', 'Borno'),
    ('crossriver', 'Cross River'),
    ('delta', 'Delta'),
    ('ebonyi', 'Ebonyi'),
    ('edo', 'Edo'),
    ('ekiti', 'Ekiti'),
    ('enugu', 'Enugu'),
    ('gombe', 'Gombe'),
    ('imo', 'Imo'),
    ('jigawa', 'Jigawa'),
    ('kaduna', 'Kaduna'),
    ('kano', 'Kano'),
    ('katsina', 'Katsina'),
    ('kebbi', 'Kebbi'),
    ('kogi', 'Kogi'),
    ('kwara', 'Kwara'),
    ('lagos', 'Lagos'),
    ('nasarawa', 'Nasawara'),
    ('niger', 'Niger'),
    ('ogun', 'Ogun'),
    ('ondo', 'Ondo'),
    ('osun', 'Osun'),
    ('oyo', 'Oyo'),
    ('plateau', 'Plateau'),
    ('rivers', 'Rivers'),
    ('sokoto', 'Sokoto'),
    ('taraba', 'Taraba'),
    ('yobe', 'Yobe'),
    ('zamfara', 'Zamfara'),
  )

  STATUS_BANK = (
    ('access', 'Access Bank Plc'),
    ('citi', 'Citibank Nigeria Limited'),
    ('eco', 'Ecobank Nigeria Plc'),
    ('fidelity', 'Fidelity Banl Plc'),
    ('monument', 'First City Monument Bank Limited'),
    ('first', 'First Bank of Nigeria Limited'),
    ('guaranty', 'Guaranty Trust Bank Plc'),
    ('keystone', 'Keystone Bank Limited'),
    ('polaris', 'Polaris Bank Limited'),
    ('stanbic', 'Stanbic IBTC Bank Plc'),
    ('standard', 'Standard Chartered'),
    ('sterling', 'Sterling Bank Plc'),
    ('titan', 'Titan Trust Bank Limited'),
    ('union', 'Union Bank of Nigeria Plc'),
    ('united', 'United Bank for Afria Plc'),
    ('unity', 'Unity Bank Plc'),
    ('wema', 'Wema Bank Plc'),
    ('zenith', 'Zenith Bank Plc'),
  )

  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='my_profile')

  first_name = models.CharField(max_length=255, blank=False, null=True)

  last_name = models.CharField(max_length=255, blank=False, null=True)

  title = models.CharField(choices=STATUS_TITLE, max_length=20, blank=False, null=False)

  gender = models.CharField(choices=STATUS_GENDER, max_length=10, blank=False, null=False)
  
  date_of_birth = models.DateField(blank=False, null=False)

  phone_number = models.CharField(max_length=20, blank=False, null=False)

  address = models.CharField(max_length=50, blank=False, null=False)

  city = models.CharField(max_length=15, blank=False, null=False)
  
  state = models.CharField(choices=STATUS_STATE, max_length=10, blank=False, null=False)

  place_of_work = models.CharField(max_length=20, blank=False, null=False)

  ippis_number = models.CharField(max_length=20, blank=False, null=False)

  salary_bank_name = models.CharField(choices=STATUS_BANK, max_length=20, blank=False, null=False)

  account_number = models.PositiveSmallIntegerField(blank=False, null=False)

  loan_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)

  tenor = models.CharField(choices=STATUS_TENOR, max_length=10, blank=False, null=False)

  referral_code = models.CharField(max_length=20, blank=True, null=True)

  created = models.DateTimeField(auto_now_add=True)

  updated = models.DateTimeField(auto_now=True)

  
  

  

 