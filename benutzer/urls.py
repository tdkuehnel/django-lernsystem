from django.urls import path

from . import views

app_name = 'benutzer'

urlpatterns = [
    path('anmeldung/',                                        views.LernsystemLoginView.as_view(),             name='anmeldung'),
]
