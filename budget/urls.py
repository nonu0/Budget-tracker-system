from django.urls import path
from .views import HomeGuest,MyUserProfile,HomeView,AllForms,AllTables,DebtView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'budget'

urlpatterns = [
    path('',HomeGuest.as_view(),name='home-guest'),
    path('home-user',HomeView.as_view(),name='home-user'),
    path('debt',DebtView.as_view(),name='debt'),
    path('forms',AllForms.as_view(),name='forms'),

    path('tables',AllTables.as_view(),name='tables'),
    path('user-profile',MyUserProfile.as_view(),name='user-profile'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)