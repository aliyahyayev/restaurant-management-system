"""
URL configuration for core project.
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from restaurant.views import home_ui  # Səhifəmizin view-nu import edirik

# Bütün marşrutları tək bir siyahıda toplayırıq:
urlpatterns = [
    # 1. Bizim Sadə UI Səhifəsi (Ana səhifə)
    path('', home_ui, name='home'), 

    # 2. Django Admin Panel
    path('admin/', admin.site.urls),

    # 3. Bizim REST API-lar
    path('api/', include('restaurant.urls')),
    
    # 4. Giriş edib token almaq üçün endpoint
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # 5. Tokenin vaxtını uzatmaq (refresh) üçün endpoint
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]