from django.urls import path
from oam_portfolio.oamViews import indexView, detailView, workshopView

urlpatterns = [
    path('home/', indexView.home, name='cv-view'),
    path('Detail/', detailView.detail, name='detail-view'),
    path('workshop/', workshopView.ws, name='ws-view')
]
