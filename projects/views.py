from django.shortcuts import render
from projects.models import Account

def account_index(request):
    accounts = Account.objects.all()
    context = {
        'accounts': accounts
    }
    return render(request, 'account_index.html', context)

def account_detail(request, pk):
    account = Account.objects.get(pk=pk)
    context = {
        'account': account
    }
    return render(request, 'account_detail.html', context)
