from django.urls import path

from .views import coin_list, coin_detail


urlpatterns = [
    path('coins', coin_list.as_view()),
    path('coins/<int:pk>/', coin_detail.as_view()),

]
