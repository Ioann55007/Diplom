from django.urls import path

from . import views
from .views import EmailVirificationView

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('edit/<int:pk>/', views.ProfileUpdate.as_view(), name='edit'),
    path('logout/', views.logout, name='logout'),
    path('delete-profile/<int:pk>/', views.DeleteProfile.as_view(), name="delete-profile"),
    path('verify/<str:email>/<uuid:code>', EmailVirificationView.as_view(), name='email_verification')
]
