from django.contrib import admin
from django.urls import path, include
from shop.views import CategoryAPIView
from shop.views import ProductAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/category/', CategoryAPIView.as_view()),
    path('api/product/', ProductAPIView.as_view())
]