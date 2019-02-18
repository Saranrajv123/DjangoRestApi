from django.urls import path
from .views import (
    StatusListSearchApiView,
    StatusApiView,
    StatusCreateApiView,
    StatusDetailApiView,
    StatusUpdateApiView,
    StatusDeleteApiView,
    )

urlpatterns = [
    path('', StatusApiView.as_view(), name='apilistview'),
    path('create/', StatusCreateApiView.as_view(), name='createapiview'),
    path('<int:id>/update/', StatusUpdateApiView.as_view(), name='updateapiview'),
    path('<int:id>/delete/', StatusDeleteApiView.as_view(), name='deleteapiview'),
    path('detail/<int:id>/', StatusDetailApiView.as_view(), name='detailApiview'),
]
