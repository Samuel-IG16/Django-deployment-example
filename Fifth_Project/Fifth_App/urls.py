from django.conf.urls import url
from Fifth_App import views

app_name = 'Fifth_App'

urlpatterns = [
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]
