from django.shortcuts import render, redirect
from .forms import YourFinanceForm
from .models import YourFinance
from django.db.models import Sum
from datetime import datetime, timedelta

def index(request):
    if request.method == 'POST':
        form = YourFinanceForm(request.POST)
        if form.is_valid():
            finance = form.save(commit=False)
            if form.cleaned_data['spend_or_receive'] == 's':
                finance.amount = -finance.amount
            finance.save()
            return redirect('index')
    else:
        form = YourFinanceForm()

    transactions = YourFinance.objects.all().order_by('date')
    context = {
        'form': form,
        'transactions': transactions
    }
    return render(request, 'finance_app/index.html', context)

def report(request):
    today = datetime.today()
    sow = today - timedelta(days=today.weekday(), weeks=1)
    eow = sow + timedelta(days=6, hours=23, minutes=59, seconds=59)
    
    print(f"Start of week: {sow}")
    print(f"End of week: {eow}")
    
    transactions = YourFinance.objects.filter(date__range=[sow, eow]).order_by('date')
    print(f"Transactions: {transactions}")
    
    total_amount = transactions.aggregate(Sum('amount'))['amount__sum'] or 0
    
    context = {
        'transactions': transactions,
        'total_amount': total_amount
    }
    return render(request, 'finance_app/report.html', context)
