from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView, TemplateView
from .models import Feed_back , User
from .forms import AddFeedbackForm, UserRegistrationForm
from .serializers import Feed_backSerializer
from django.contrib.auth import login
from rest_framework import viewsets
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly




# Create your views here.

class HomeView(TemplateView):
    template_name = 'prod_feedback/home.html'


class FeedbackView(ListView):
    model = Feed_back
    template_name = 'prod_feedback/feedback.html'
    context_object_name = 'feedbacks'


class ThankYouView(TemplateView):
    model = Feed_back
    template_name = 'prod_feedback/thank_you.html'
    context_object_name = 'feedbacks'


class AddFeedbackView(TemplateView):
    model = Feed_back
    template_name = 'prod_feedback/add_feedback.html'
    context_object_name = 'feedbacks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AddFeedbackForm()
        return context

    def post(self, request, *args, **kwargs):
        form = AddFeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            # Create Team member
            feedback = form.save(commit=False)
            feedback.save()
            return redirect('prod_feedback:home')
        return self.render_to_response(self.get_context_data(form=form))




# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     name = models.CharField(max_length=100)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(default=timezone.now)

#     objects = UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name']

#     def __str__(self):
#         return self.email



class UserRegisterView(TemplateView):
    template_name = 'prod_feedback/user_register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserRegistrationForm()
        return context

    def post(self, request, *args, **kwargs):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('prod_feedback:dashboard')
        return self.render_to_response(self.get_context_data(form=form))


class Feed_backViewSet(viewsets.ModelViewSet):
    queryset = Feed_back.objects.filter(is_visible=True)
    serializer_class = Feed_backSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class UserDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'prod_feedback/user_dashboard.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['featured_books'] = Feed_back.objects.filter(is_visible=True)[:10]
    #     return context
