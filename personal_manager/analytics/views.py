from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .models import TestModel


class AnalyticsDashboardView(TemplateView):
    template_name = 'analytics/index.html'
    model = TestModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = TestModel.objects.all()[0].name
        return context

    def post(self, request, *args, **kwargs):
        TestModel.objects.create(name="piter")
        return redirect('/')

