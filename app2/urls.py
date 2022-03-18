from app2.views import a2_gova
from django.urls import path
app_name='app2'
urlpatterns=[
    path('a2_gova/',a2_gova,name='a2_gova'),
]