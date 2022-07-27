from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("cart/", views.cart, name="cart"),
    path("login/", views.login_user, name='login'),
    path("product/", views.product, name="product"),
    path("details/<str:pk>/", views.details, name="details"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('logout/', views.logoutUser, name='logout')
]