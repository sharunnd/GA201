from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('signup/admin/', views.admin_signup, name='admin_signup'),
    path('signup/customer/', views.customer_signup, name='customer_signup'),
    path('login/admin/', views.admin_login, name='admin_login'),
    path('login/customer/', views.customer_login, name='customer_login'),
]
