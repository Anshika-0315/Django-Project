"""
URL configuration for Feedback project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from . import views


# app_name = 'prod_feedback'

# router = DefaultRouter()
# router.register(r'prod_feedback', views.Feed_backViewSet, basename='feedback')


# urlpatterns = [
#     path('', views.HomeView.as_view(), name='home'),
#     path('feedback/', views.FeedbackView.as_view(), name='feedback'),
#     path('addfeedback/', views.AddFeedbackView.as_view(), name='add_feedback'),
#     path('thankyou/', views.ThankYouView.as_view(), name='thank_you'),
# ]





from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
# from . import views


admin.site.site_header = "Feedback Admin"
admin.site.site_title = "Feedback Admin Portal"
admin.site.index_title = "Welcome to Feedback Management"



# app_name = 'prod_feedback'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('prod_feedback.urls')),  # Add prod_feedback app URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Login, logout
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

