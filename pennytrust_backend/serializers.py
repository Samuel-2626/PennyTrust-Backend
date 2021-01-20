# from rest_framework import serializers

# from allauth.account import app_settings as allauth_settings
# from allauth.utils import email_address_exists
# from allauth.account.adapter import get_adapter
# from allauth.account.utils import setup_user_email

# class RegisterSerializer(serializers.Serializer):

#   STATUS_TENOR = (
#     ('2', '2 Months'),
#     ('3', '3 Months'),
#     ('4', '4 Months'),
#     ('5', '5 Months'),
#     ('6', '6 Months'),
#     ('7', '7 Months'),
#     ('8', '8 Months'),
#     ('9', '9 Months'),
#     ('10', '10 Months'),
#     ('11', '11 Months'),
#     ('12', '12 Months'),
#     ('13', '13 Months'),
#     ('14', '14 Months'),
#     ('15', '15 Months'),
#     ('16', '16 Months'),
#     ('17', '17 Months'),
#     ('18', '18 Months'),
    
#   )

#   STATUS_TITLE = (
#     ('mr', 'Mr'),
#     ('mrs', 'Mrs'),
#     ('alhaji', 'Alhaji'),
#     ('chief', 'Chief'),
#     ('dr', 'Dr'),
#   )

#   STATUS_GENDER = (
#     ('male', 'Male'),
#     ('female', 'Female'),
#   )

#   STATUS_STATE = (
#     ('abia', 'Abia'),
#     ('adamawa', 'Adamawa'),
#     ('akwaibom', 'Akwa Ibom'),
#     ('anambra', 'Anambra'),
#     ('bauchi', 'Bauchi'),
#     ('bayelsa', 'Bayelsa'),
#     ('benue', 'Benue'),
#     ('borno', 'Borno'),
#     ('crossriver', 'Cross River'),
#     ('delta', 'Delta'),
#     ('ebonyi', 'Ebonyi'),
#     ('edo', 'Edo'),
#     ('ekiti', 'Ekiti'),
#     ('enugu', 'Enugu'),
#     ('gombe', 'Gombe'),
#     ('imo', 'Imo'),
#     ('jigawa', 'Jigawa'),
#     ('kaduna', 'Kaduna'),
#     ('kano', 'Kano'),
#     ('katsina', 'Katsina'),
#     ('kebbi', 'Kebbi'),
#     ('kogi', 'Kogi'),
#     ('kwara', 'Kwara'),
#     ('lagos', 'Lagos'),
#     ('nasarawa', 'Nasawara'),
#     ('niger', 'Niger'),
#     ('ogun', 'Ogun'),
#     ('ondo', 'Ondo'),
#     ('osun', 'Osun'),
#     ('oyo', 'Oyo'),
#     ('plateau', 'Plateau'),
#     ('rivers', 'Rivers'),
#     ('sokoto', 'Sokoto'),
#     ('taraba', 'Taraba'),
#     ('yobe', 'Yobe'),
#     ('zamfara', 'Zamfara'),
#   )

#   STATUS_BANK = (
#     ('access', 'Access Bank Plc'),
#     ('citi', 'Citibank Nigeria Limited'),
#     ('eco', 'Ecobank Nigeria Plc'),
#     ('fidelity', 'Fidelity Banl Plc'),
#     ('monument', 'First City Monument Bank Limited'),
#     ('first', 'First Bank of Nigeria Limited'),
#     ('guaranty', 'Guaranty Trust Bank Plc'),
#     ('keystone', 'Keystone Bank Limited'),
#     ('polaris', 'Polaris Bank Limited'),
#     ('stanbic', 'Stanbic IBTC Bank Plc'),
#     ('standard', 'Standard Chartered'),
#     ('sterling', 'Sterling Bank Plc'),
#     ('titan', 'Titan Trust Bank Limited'),
#     ('union', 'Union Bank of Nigeria Plc'),
#     ('united', 'United Bank for Afria Plc'),
#     ('unity', 'Unity Bank Plc'),
#     ('wema', 'Wema Bank Plc'),
#     ('zenith', 'Zenith Bank Plc'),
#   )

#   email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
#   loan_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
#   tenor = serializers.ChoiceField(choices=STATUS_TENOR, required=True, write_only=True)
#   title = serializers.ChoiceField(choices=STATUS_TITLE, required=True, write_only=True)
#   first_name = serializers.CharField(required=True, write_only=True)
#   last_name = serializers.CharField(required=True, write_only=True)
#   date_of_birth = serializers.DateField(required=True, write_only=True)
#   gender = serializers.ChoiceField(choices=STATUS_GENDER, required=True, write_only=True)
#   referral_code = serializers.CharField(required=False, write_only=True)
#   phone_number = serializers.IntegerField(required=True, write_only=True)
#   address = serializers.CharField(required=True, write_only=True)
#   city = serializers.CharField(required=True, write_only=True)
#   state = serializers.ChoiceField(choices=STATUS_STATE, required=True, write_only=True)
#   place_of_work = serializers.CharField(required=True, write_only=True)
#   ippis_number = serializers.CharField(required=True, write_only=True)
#   salary_bank_name = serializers.ChoiceField(choices=STATUS_BANK, required=True, write_only=True)
#   account_number = serializers.IntegerField(required=True, write_only=True)

#   def validate_email(self, email):
#     email = get_adapter().clean_email(email)
#     if allauth_settings.UNIQUE_EMAIL:
#       if email and email_address_exists(email):
#         raise serializers.ValidationError(
#       ("A user is already registered with this e-mail address.")
#       )
#     return email

#   def get_cleaned_data(self):
#     return {
#       'first_name': self.validated_data.get('first_name', ''),
#       'last_name': self.validated_data.get('last_name', ''),
#       'email': self.validated_data.get('email', ''),
#       'title': self.validated_data.get('title', ''),
#       'loan_amount': self.validated_data.get('loan_amount', ''),
#       'tenor': self.validated_data.get('tenor', ''),
#       'date_of_birth': self.validated_data.get('date_of_birth', ''),
#       'gender': self.validated_data.get('gender', ''),
#       'referral_code': self.validated_data.get('referral_code', ''),
#       'address': self.validated_data.get('address', ''),
#       'city': self.validated_data.get('city', ''),
#       'state': self.validated_data.get('state', ''),
#       'place_of_work': self.validated_data.get('place_of_work', ''),
#       'ippis_number': self.validated_data.get('ippis_number', ''),
#       'salary_bank_name': self.validated_data.get('salary_bank_name', ''),
#       'account_number': self.validated_data.get('account_number', ''),
#     }

#   def save(self, request):
#     adapter = get_adapter()
#     user = adapter.new_user(request)
#     self.cleaned_data = self.get_cleaned_data()
#     adapter.save_user(request, user, self)
#     setup_user_email(request, user, [])
#     user.save()
#     return user