from django.urls import path
from.views import HomePageView, AboutPageView, DataView, DiseaseView, MapsView, PredictionView,LoginView, RegisterView, HelpView, APView,FeedbackView


urlpatterns = [
   path('register/register/', RegisterView.as_view(), name='register'),
   path('login/', LoginView.as_view(), name='login'),
   path('login/AdminPanel/', APView.as_view(), name='AdminPanel'),
   path('help/', HelpView.as_view(), name='help'),
   path('disease/', DiseaseView.as_view(), name='disease'),
   path('maps/', MapsView.as_view(), name='maps'),
   path('prediction/', PredictionView.as_view(), name='prediction'),
   path('feedback/',FeedbackView.as_view(), name='feedback'),
   path('data/', DataView.as_view(), name='data'),
   path('about/', AboutPageView.as_view(), name='about'),
   path('', HomePageView.as_view(), name='home'),
]
