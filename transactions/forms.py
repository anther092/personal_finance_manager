from django import forms
from accounts.models import AccountsModel
from .models import Transactions


class AccountManipulation(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ["where", "how_much", "category", "time", "acc"]

        widgets = {
            "time": forms.DateTimeInput(
                attrs={"type": "datetime-local"},
                format="%Y-%m-%dT%H:%M",
            )
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields["time"].input_formats = ["%Y-%m-%dT%H:%M"]

class AddNewAcc(forms.ModelForm):
    class Meta:
        model = AccountsModel
        fields = ["name_acc"]

