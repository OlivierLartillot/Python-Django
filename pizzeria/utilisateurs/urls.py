from django.urls import path, include

app_name = 'utilisateurs'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
]