from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('homeflow', views.index1, name='indexflow'),
    path('reports/', views.genreports, name='genrep'),
    path('search/', views.search, name='searchid'),
    path('5hpac/', views.ac5hprep, name='5hprep'),
    path('3hpac/', views.ac3hprep, name='3hprep'),
    path('datareport/', views.datarep, name='dailydata'),
    path('datareport1/', views.datarep1, name='dailydata1'),
    path('openIds/<rmsid>/', views.openId, name='idwise'),
    # path('log', views.logoutpage, name='lo'),
    # path('GetInvDaysData/', views.GetInvDaysData, name='apiDayData'),
    # path('GetInvMonthData/', views.GetInvMonthData, name='apiMonthData'),
]