from django.urls import path
from .views import LoginAPI,RegisterAPI
from knox import views as knox_views
urlpatterns = [
  path("login",LoginAPI.as_view()),
  path('register',RegisterAPI.as_view()),
  path('logout', knox_views.LogoutView.as_view(), name='logout'),
  path('logoutall', knox_views.LogoutAllView.as_view(), name='logoutall')
]