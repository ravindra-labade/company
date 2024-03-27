from django.shortcuts import render, redirect
from .forms import CompanyForm
from .models import Company
from django.contrib.auth.decorators import login_required


def add_company(request):
    template_name = 'company/add.html'
    form = CompanyForm()
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)


def show_company(request):
    template_name = 'company/show.html'
    companies = Company.objects.all()
    context = {'companies': companies}
    return render(request, template_name, context)


def update_company(request, pk):
    template_name = 'company/add.html'
    obj = Company.objects.get(id=pk)
    form = CompanyForm(instance=obj)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)



def delete_company(request, pk):
    obj = Company.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    return render(request, 'company/confirm.html')