from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import date
from . models import CompanyBranch, Company, KeyPerfomanceIndicator, FrequentlyAskedQuestion
from staff.models import Staff, Pipeline

# Create your views here.
@login_required(login_url="/account/login/")
def company(request):
    user = request.user
    staff = get_object_or_404(Staff, user=user)
    companys = Company.objects.order_by('id')[:1]
    kpis = KeyPerfomanceIndicator.objects.all()
    today = date.today()
    interactions = user.interaction_set.all()
    latest_interactions = interactions.order_by('-id')[:3]
    todays_interactions = interactions.filter(date_created__date=today).count()

    pipelin =Pipeline.objects.filter(created_by=user, done=False, postponed=False, pipeline_date=today)
    todays_pipelines_count = pipelin.count()
    todays_pipelines = pipelin.order_by('-id')[:3]

    


    branch = staff.branch
    context = {
        'companys': companys,
        'branch': branch,
        'kpis': kpis,
        'todays_interactions' : todays_interactions,
        'latest_interactions': latest_interactions,

        'todays_pipelines': todays_pipelines,
        'todays_pipelines_count': todays_pipelines_count
    }
    return render(request, 'company.html', context)

@login_required(login_url="/account/login/")
def dashboard(request):
    companys = Company.objects.order_by('id')[:1]
    user = request.user
    today = date.today()
    interactions = user.interaction_set.all()
    latest_interactions = interactions.order_by('-id')[:3]
    todays_interactions = interactions.filter(date_created__date=today).count()

    pipelin =Pipeline.objects.filter(created_by=user, done=False, postponed=False, pipeline_date=today)
    todays_pipelines_count = pipelin.count()
    todays_pipelines = pipelin.order_by('-id')[:3]
    context = {
        'todays_interactions' : todays_interactions,
        'companys': companys,
        'latest_interactions': latest_interactions,

        'todays_pipelines': todays_pipelines,
        'todays_pipelines_count': todays_pipelines_count
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url="/account/login/")
def faq(request):
    companys = Company.objects.order_by('id')[:1]
    user = request.user
    today = date.today()
    interactions = user.interaction_set.all()
    latest_interactions = interactions.order_by('-id')[:3]
    todays_interactions = interactions.filter(date_created__date=today).count()

    pipelin =Pipeline.objects.filter(created_by=user, done=False, postponed=False, pipeline_date=today)
    todays_pipelines_count = pipelin.count()
    todays_pipelines = pipelin.order_by('-id')[:3]

    faqs = FrequentlyAskedQuestion.objects.order_by('-id')
    context = {
        'todays_interactions' : todays_interactions,
        'companys': companys,
        'latest_interactions': latest_interactions,
        'faqs': faqs,

        'todays_pipelines': todays_pipelines,
        'todays_pipelines_count': todays_pipelines_count
    }
    return render(request, 'faq.html', context)

@login_required(login_url="/account/login/")
def addKPI(request):

    if request.method == 'POST':
       KPI_name = request.POST['KPI_name']
       KPI_defination = request.POST['KPI_defination']
       why_is_it_important = request.POST['why_is_it_important']

       kpi=KeyPerfomanceIndicator.objects.create(KPI_name= KPI_name, KPI_defination=KPI_defination, why_is_it_important=why_is_it_important)
       kpi.save()
       messages.success(request, f'You have successfully added {KPI_name} as one  of your KPI !!!')
       return redirect('company')