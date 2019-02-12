"""auto_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from share.views import HomeView, MyView, SearchView, DisplayView  # 导入 视图函数中的对象
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView.as_view(),name="home"),
    path('my/',MyView.as_view(),name="MY"),
    path('s/<int:code>/', DisplayView.as_view()),
    # /s/(?P<code>\d+ 使用了组匹配的方式 匹配code任意长度的数字，如/s/123456，将123456传给 DisplayView,这里的 code 必须和视图函数的 code 保持一致。
    path('search/',SearchView.as_view(),name="search"),
]
