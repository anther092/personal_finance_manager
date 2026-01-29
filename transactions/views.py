from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView
from .forms import AccountManipulation, AddNewAcc
from accounts.models import AccountsModel
from .models import Transactions


class TransactionsView(TemplateView):
    template_name = 'transactions/transactions.html'

    def post(self, request, *args, **kwargs):
        form_id = request.POST.get("form_id")

        if form_id == "transactions":
            tx_form = AccountManipulation(request.POST)
            if tx_form.is_valid():
                Transactions.objects.create(where=tx_form.data['where'],
                                            time=tx_form.data['time'],
                                            how_much=tx_form.data['how_much'],
                                            category=tx_form.data['category'],
                                            acc=tx_form.data['acc'],
                                            )

                old_cash = float(AccountsModel.objects.filter(name_acc=tx_form.data['acc'])[0].cash)
                AccountsModel.objects.\
                    filter(name_acc=tx_form.data['acc']).\
                    update(cash=old_cash+float(tx_form.data['how_much']))

                redirect("/transactions")
        elif form_id == "account":
            acc_form = AddNewAcc(request.POST)
            if acc_form.is_valid():
                AccountsModel.objects.create(name_acc=acc_form.data['name_acc'], cash=0)
                return redirect("/transactions")

        return redirect("/transactions")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        formAccManipulation = AccountManipulation(self.request.POST or None)
        formAddNewAcc = AddNewAcc(self.request.POST or None)

        if formAccManipulation.is_valid():
            pass

        if formAddNewAcc.is_valid():
            pass

        context['formAccManipulation'] = formAccManipulation
        context['formAddNewAcc'] = formAddNewAcc

        return context


