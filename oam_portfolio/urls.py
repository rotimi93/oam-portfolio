from django.urls import path
from oam_portfolio.views import home, detail,ws

urlpatterns = [
    path('', home, name='cv-view'),
    path('detail/', detail, name='detail-view'),
    path('workshop/', ws, name='ws-view')
]
