from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from . views import UserRegViewSet, logoutViewSet

router = DefaultRouter()
router.register('register', UserRegViewSet, basename='register')

urlpatterns = [
    path('', include(router.urls)),
    path('auth-api/', include('rest_framework.urls')),
    path('login/', views.obtain_auth_token),
    path('logout/', logoutViewSet.as_view()),
]
