from django.urls import include, re_path
from rest_framework.routers import DefaultRouter

from crud_api import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'task', views.TaskViewSet, 'task')
router.register(r'user', views.UserViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    re_path('', include(router.urls))
]