from django.contrib import admin
from django.urls import path
from .views import (
	SpotDetail,
	SpotList,
)

urlpatterns = [
    path('spots', SpotList.as_view(), name='spot_detail'),
    path('spots/<slug:id>', SpotDetail.as_view(), name='spot detail')
]
