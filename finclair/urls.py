from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('transactions/', include('transactions.urls')),
    path('budgets/', include('budgets.urls')),
    path('objectifs/', include('objectifs.urls')),
    path('dettes/', include('dettes.urls')),
    path('alertes/', include('alertes.urls')),
    path('statistiques/', include('statistiques.urls')),
]