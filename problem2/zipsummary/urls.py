from django.urls import path

from . import views

urlpatterns = [
    path('', views.ZipFormView.as_view(), name='zipform'),
]
