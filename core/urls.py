from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('api/token/',TokenObtainPairView.as_view()),
    path('api/token/refresh/',TokenRefreshView.as_view()),
    path('api/token/verify/',TokenVerifyView.as_view()),
    path('admin/', admin.site.urls),
    path('',include('budget.urls')),
    path('authentication/',include('authentication.urls'))
]
