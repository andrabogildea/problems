"""cbszip URL Configuration"""

from django.urls import include, path

urlpatterns = [
    # mount zipsummary as root
    path('', include('zipsummary.urls'))
]
