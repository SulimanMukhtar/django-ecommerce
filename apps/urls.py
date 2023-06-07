from django.urls import path

from apps.views import TestView

urlpatterns = [
    path('test', TestView.as_view({'get': 'test_method'}))
]
