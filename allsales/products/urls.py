from django.urls import path
from . import views

urlpatterns = [
    path('', views.say_hello),
    path('get-products/', views.get_products),
    path('generic/create/', views.product_create_list_api_view),
    path('generic/', views.product_list_api_view),
    path('generic/<int:pk>/', views.product_detail_view),
    path('generic/<int:pk>/update/', views.product_update_api_view),
    path('generic/<int:pk>/delete/', views.product_destroy_api_view),
    path('alt/', views.product_alt_view),
    path('alt/<int:pk>/', views.product_alt_view),

    # Mixins
    path('mixins/', views.model_mixin_view),
    path('mixins/<int:pk>/', views.model_mixin_view),
    path('mixins/<int:pk>/update/', views.model_mixin_view),
    path('mixins/<int:pk>/delete/', views.model_mixin_view),
]
