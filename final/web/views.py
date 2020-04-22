from django.shortcuts import render,redirect
from django.views.generic import TemplateView



class HomePageView(TemplateView):
    template_name = 'home.html'


class RegisterView(TemplateView):
    template_name = 'Register.html'


class LoginView(TemplateView):
    template_name = 'Login.html'


class AboutPageView(TemplateView):
    template_name = 'About.html'


class DataView(TemplateView):
    template_name = 'Data.html'


class DiseaseView(TemplateView):
    template_name = 'Disease Description.html'


class MapsView(TemplateView):
    template_name = 'Maps.html'


class PredictionView(TemplateView):
    template_name = 'Prediction.html'


class FeedbackView(TemplateView):
    template_name = 'Feedback.html'


class APView(TemplateView):
    template_name = 'AdminPanel.html'


class HelpView(TemplateView):
    template_name = 'Help.html'



