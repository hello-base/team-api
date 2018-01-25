"""
URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""
from django.contrib import admin
from django.urls import include, path

from rest_framework import routers

from casters.views import UserViewSet
from episodes.views import CornerViewSet, EpisodeViewSet
from news.views import ItemViewSet
from viewings.views import ViewingViewSet


router = routers.DefaultRouter()
router.register(r'casters', UserViewSet)
router.register(r'episodes', EpisodeViewSet)
router.register(r'corners', CornerViewSet)
router.register(r'items', ItemViewSet)
router.register(r'viewings', ViewingViewSet)

urlpatterns = [
    #
    path('', include(router.urls)),

    # Administration system.
    path('admin/', admin.site.urls),
]
