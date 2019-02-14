from django.urls import path
from .views import (
    UpdateModelDetailAPIView,
    UpdateModelListAPIView,
)

urlpatterns = [
    path('', UpdateModelListAPIView.as_view(), name="apilistview"),
    path('<int:id>/', UpdateModelDetailAPIView.as_view(), name='updatedetailview'),
]