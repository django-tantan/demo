from django.conf.urls import url
from app import views


urlpatterns =[
    url(r'^tantan/$',views.register,name='register'),

]