from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='website-home'),
    path('about/', views.about, name='website-about'),
    path('sign_up',views.sign_up, name='sign_up'),
    path('survey_thanks',views.survey_thanks, name='survey_thanks'),
    path('send_surveys',views.send_surveys, name='send_surveys')
]
