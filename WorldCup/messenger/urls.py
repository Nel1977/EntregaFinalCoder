from django.urls import path
from .views import ThreadList, ThreadDetail

urlpatterns = [
    path('', ThreadList.as_view(), name="list"),
    path('thread/<int:pk>', ThreadDetail.as_view(), name="detail"),
]