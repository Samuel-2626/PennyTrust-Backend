from django.contrib import admin

from .models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
  list_display = ('user', 'title', 'first_name', 'last_name', 'gender', 'date_of_birth', 'phone_number', 'state', 'place_of_work', 'loan_amount', 'tenor')
  list_filter = ('state', 'loan_amount', 'tenor', 'gender', 'title')
  search_fields = ('first_name', 'last_name')
  raw_id_fields = ('user',)
  date_hierarchy = 'created'
  ordering = ('first_name', 'last_name')


