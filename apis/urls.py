from django.urls import path

from .views import ProfileDetail, GetUsersEmail, GetProfilesIppisNumber, GetProfilesNumber, GetProfilesAccountNumber, GetUser, ProfileCreate, GetProfile


urlpatterns = [
    path('profile/', ProfileCreate.as_view()),
    path('profile/<int:pk>/', ProfileDetail.as_view()),
    path('get_users_email/', GetUsersEmail.as_view()),
    path('get_profiles_ippis_number/', GetProfilesIppisNumber.as_view()),
    path('get_profiles_phone_number/', GetProfilesNumber.as_view()),
    path('get_profiles_account_number/', GetProfilesAccountNumber.as_view()),
    path('get_user/<str:email>', GetUser.as_view()),
    path('get_profile/<int:user>', GetProfile.as_view()),
]
