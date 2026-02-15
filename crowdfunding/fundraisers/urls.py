from django.urls import path
from . import views

urlpatterns = [
    path('fundraisers/', views.FundraiserList.as_view()),
    path('fundraisers/<int:pk>/', views.FundraiserDetail.as_view()),
    path('pledges/', views.PledgeList.as_view()),
    path('discovery/favourite/<int:pk>/', views.FavouriteCreate.as_view()),
    path('discovery/favourites/', views.FavouriteList.as_view()),
    path('detail/enquire/<int:pk>/', views.EnquiryCreate.as_view()),
]