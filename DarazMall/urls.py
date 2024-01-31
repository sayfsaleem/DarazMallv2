"""
URL configuration for DarazMall project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from main import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.LoginView.as_view(),name='login'),
    path('signup/',views.RegisterView.as_view(),name='register'),
    path('plans/',views.PlansView.as_view(),name='plans'),
    path('payment/<slug:plan>/',views.PaymentView.as_view(),name='Payment'),
    path('pending/',views.PaymentPendingView.as_view(),name='PaymentPending'),
    path('dashboard/',views.DashboardView.as_view(),name='dashboard'),
    path('rate/<int:id>/',views.Rate.as_view(),name='rate'),
    path('work/',views.WorkView.as_view(),name='work'),
    path('profile/',views.Profile.as_view(),name='profile'),
    path('wallet/',views.Wallet.as_view(),name='wallet'),
    path('team/',views.TeamView.as_view(),name='team'),
    path('signup/refer/<slug:invite>',views.ReferView.as_view(),name='refer'),
    path('ranking/',views.RewardView.as_view(),name='reward'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('',views.HomeView.as_view(),name='home'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
