from django.urls import path,re_path
from AppTwo import views

urlpatterns = [
    re_path(r'^$',views.help,name='help'),
    # re_path(r'^help/',views.help,name='help'),
]
