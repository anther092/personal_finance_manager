from django.db.models import Sum
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from accounts.models import AccountsModel
from transactions.models import Transactions
from .forms import PeriodForm


class AnalyticsDashboardView(TemplateView):
    template_name = 'analytics/index.html'

    def __get_period_transactions(self, income):
        form = PeriodForm(self.request.GET or None)
        qs = Transactions.objects.all()

        print(form.data)
        if form.is_valid():
            start = form.cleaned_data.get('start')
            end = form.cleaned_data.get('end')

            if start and end:
                qs = qs.filter(time__range=(start, end))
            elif start:
                qs = qs.filter(time__gte=start)
            elif end:
                qs = qs.filter(time__lte=end)

        if income:
            qs = qs.filter(how_much__gt=0)
        elif not income:
            qs = qs.filter(how_much__lt=0)

        return qs.aggregate(total=Sum("how_much"))["total"]

    def get_context_data(self, **kwargs):
        form = PeriodForm()

        context = super().get_context_data(**kwargs)
        context['total_balance'] = AccountsModel.objects.aggregate(total=Sum("cash"))["total"]
        context['form'] = form
        context['income'] = self.__get_period_transactions(True)
        context['expenses'] = self.__get_period_transactions(False)
        context['accounts'] = AccountsModel.objects.all()
        context['last_transactions'] = Transactions.objects.order_by('-id')[:10]

        return context


