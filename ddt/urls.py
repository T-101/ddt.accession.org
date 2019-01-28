from django.urls import path

from ddt.views import IndexView, FuneralView, WallView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('funeral/', FuneralView.as_view(), name="funeral"),
    path('wall/', WallView.as_view(), name="wall")
]
