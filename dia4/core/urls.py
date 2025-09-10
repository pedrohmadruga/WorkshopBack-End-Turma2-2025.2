from django.urls import path
from . import views

urlpatterns = [
    path('consulta/', views.ViaCepFormView.as_view(), name='consulta')
]
