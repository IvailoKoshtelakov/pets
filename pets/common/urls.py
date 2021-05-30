from django.urls import path

from pets.common.views import landing_page, testing_view

urlpatterns = [
    path('', landing_page),
    path('testing', testing_view, name='testing'),

  ]