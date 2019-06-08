from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.loadLoginPage, name='adminLogin'),
    url(r'^verifyLogin$', views.verifyLogin, name='verifyLogin'),
    url(r'^logout$', views.logout, name='logout')
]