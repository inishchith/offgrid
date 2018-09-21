from django.conf.urls import url
from app import views

# SET THE NAMESPACE!
app_name = 'app'


urlpatterns=[
    url(r'^$',views.appindex,name='appindex'),
    url(r'^map/$',views.map,name='map'),
]