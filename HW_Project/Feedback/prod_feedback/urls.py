# from django.contrib import admin
# from django.urls import path , include
# from django.conf import settings
# from django.conf.urls.static import static
# from . import views


# admin.site.site_header = "Feedback Admin"
# admin.site.site_title = "Feedback Admin Portal"
# admin.site.index_title = "Welcome to Feedback Management"



# app_name = 'prod_feedback'

# urlpatterns = [
#     path('', views.HomeView.as_view(), name='home'),
#     path('feedback/', views.FeedbackView.as_view(), name='feedback'),
#     path('addfeedback/', views.AddFeedbackView.as_view(), name='add_feedback'),
#     path('thankyou/', views.ThankYouView.as_view(), name='thank_you'),
#     path('accounts/', include('django.contrib.auth.urls')),  # Login, logout
# ]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




# from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


app_name = 'prod_feedback'

router = DefaultRouter()
router.register(r'prod_feedback', views.Feed_backViewSet, basename='feedback')


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('feedback/', views.FeedbackView.as_view(), name='feedback'),
    path('addfeedback/', views.AddFeedbackView.as_view(), name='add_feedback'),
    path('thankyou/', views.ThankYouView.as_view(), name='thank_you'),
    path('register/', views.UserRegisterView.as_view(), name='user_register'),
    path('dashboard/', views.UserDashboardView.as_view(), name='dashboard'),
]
