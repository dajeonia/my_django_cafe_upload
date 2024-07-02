from django.urls import path

from . import views

app_name="api"

urlpatterns = [
    path('url/', views.getNaverUrl, name='get_naver_url'),
]
