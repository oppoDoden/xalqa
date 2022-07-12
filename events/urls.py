from django.urls import path, include
from .views import EventList, DetailEvent, DeleteDataBase, ImgList, bodyText, byName, delApi

urlpatterns = [
	path('name/<str:name>/', byName, name='FilterByName'),
	path('text/<int:pk>/', bodyText, name='bodyText'),
	path('<int:pk>/', DetailEvent.as_view(), name='detailevent'),
	path('deleteDataBase/',delApi, name='deleteDB'),
	path('img/', ImgList.as_view(), name='save_img'),
	path('', EventList.as_view(), name='eventlist'),
]
