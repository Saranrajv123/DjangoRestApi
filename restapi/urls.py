"""restapi URL Configuration

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
from updates.views import (
    Json_CBV2, 
    Json_CBV2, 
    json_example_view, 
    serializedDetailView,
    serializedListView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jsonview1', Json_CBV2.as_view(), name='json_view1'),
    path('jsonview2', Json_CBV2.as_view(), name='json_view2'),
    path('jsonserializedeatil', serializedDetailView.as_view(), name='jsonserializedeatil'),
    path('json/example', json_example_view),
    path('serialize/data', serializedListView.as_view(), name='serializedListView')


]
