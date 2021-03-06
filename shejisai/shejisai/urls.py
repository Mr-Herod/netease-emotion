"""shejisai URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from netease import views
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sign_up/',views.signup,name='signup'),
    url(r'^sign_in/',views.signin,name='signin'),
    url(r'^index/',views.index,name='index'),
    url(r'^profile/',views.profile,name='profile'),
    url(r'^analyse/',views.analyse,name='analyse'),
    url(r'^history/',views.history,name='history'),
    url(r'^like/',views.like,name='like'),
    url(r'^add/',views.add,name='add'),
    url(r'^recommend/',views.recommend,name='recommend'),
    url(r'^/',views.signin,name='signin'),
    url(r'^',views.signin,name='signin'),
]
