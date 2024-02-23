from django.urls import path
from .views import LivePriceView

urlpatterns = [
    path('live_price/', LivePriceView.as_view(), name='live_time'),
]   