
from django.shortcuts import render, redirect, get_object_or_404, HttpResponsePermanentRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from datetime import date, datetime, time
from dal import autocomplete
from django.contrib import messages
from . models import Pipeline, PipelineNotes, Staff, Target, Report
from . forms import AddPipelineForm, AddReportForm, AddTargetForm
from customers.models import Customer
from company.models import Company, CompanyBranch

# Create your views here.

def CustomerAutocomplete(request):
   if 'term' in request.GET:
        term = request.GET.get('term')
        customers = Customer.objects.filter(name__icontains=term).values_list('name', flat=True)
        return JsonResponse(list(customers), safe=False)
   return JsonResponse([], safe=False)

@login_required(login_url="/account/login/")
def staffs(request):
   
    companys = Company.objects.order_by('id')[:1]
    user = request.user
    today = date.today()
    interactions = user.interaction_set.all()
    latest_interactions = interactions.order_by('-id')[:3]
    todays_interactions = interactions.filter(date_created__date=today).count()

    pipelines =Pipeline.objects.filter(created_by=user, done=False, postponed=False, pipeline_date=today)
    todays_pipelines_count = pipelines.count()
    todays_pipelines = pipelines.order_by('-id')[:3]

    all_staffs = Staff.objects.all()
    staffs = Staff.objects.filter(id=user.staff.id) 

    staff_id = request.GET.get('staff', 0)
    branch_id = request.GET.get('branch', 0)
    company_id = request.GET.get('company', 0)
    query = request.GET.get('query')
    # if query:
    #     leads = all_leads.filter(Q(name__icontains=query)| Q(description__icontains=query) |Q( phone__icontains=query))
   
    if staff_id :
        staffs = staffs

    if branch_id :
        staffs = all_staffs.filter(branch__id=branch_id )
    if company_id :
        staffs = all_staffs


    context = {
        'staffs' : staffs,
        'query': query,

        'todays_interactions' : todays_interactions,
        'companys': companys,
        'latest_interactions': latest_interactions,
        'todays_pipelines': todays_pipelines,
        'todays_pipelines_count': todays_pipelines_count
    }
    return render(request, 'staffs.html', context)

@login_required(login_url="/account/login/")
def ViewStaff(request, id ):
    staff =get_object_or_404(Staff, id=id)

    companys = Company.objects.order_by('id')[:1]
    user = request.user
    today = date.today()
    interactions = user.interaction_set.all()
    latest_interactions = interactions.order_by('-id')[:3]
    todays_interactions = interactions.filter(date_created__date=today).count()

    pipelines =Pipeline.objects.filter(created_by=user, done=False, postponed=False, pipeline_date=today)
    todays_pipelines_count = pipelines.count()
    todays_pipelines = pipelines.order_by('-id')[:3]

    targets = Target.objects.filter( created_by=staff.user, timeline="Today", date_created__date=today ) 
    reports = Report.objects.filter( created_by=staff.user, date_created__date=today ) 

    today_staff_pipelines=Pipeline.objects.filter(created_by=staff.user, pipeline_date=today)
    today_staff_pipelines_count =  today_staff_pipelines.count()

    context = {
        'staff' : staff,
        'targets': targets,
        'reports': reports,
        'today_staff_pipelines' :  today_staff_pipelines,
        'today_staff_pipelines_count': today_staff_pipelines_count,

        'todays_interactions' : todays_interactions,
        'companys': companys,
        'latest_interactions': latest_interactions,
        'todays_pipelines': todays_pipelines,
        'todays_pipelines_count': todays_pipelines_count,

    }
    return render(request, 'view-staff.html', context)

@login_required(login_url="/account/login/")
def addStaff(request):
    companys = Company.objects.order_by('id')[:1]
    branches = CompanyBranch.objects.all()

    user = request.user
    today = date.today()
    interactions = user.interaction_set.all()
    latest_interactions = interactions.order_by('-id')[:3]
    todays_interactions = interactions.filter(date_created__date=today).count()

    pipelin =Pipeline.objects.filter(created_by=user, done=False, postponed=False, pipeline_date=today)
    todays_pipelines_count = pipelin.count()
    todays_pipelines = pipelin.order_by('-id')[:3]

    if request.method == 'POST':
       username = request.POST['username']
       first_name = request.POST['first_name']
       last_name = request.POST['last_name']
       email = request.POST['email']
       phone = request.POST['phone']
       role = request.POST['role']
       password = request.POST['password']
       branch = request.POST['branch']
       admin = request.POST['admin']

       company_branch = get_object_or_404(CompanyBranch, id=branch)

       if User.objects.filter(username=username):
           messages.success(request, "username already exists!!!")
           return redirect('add_staff')
       user=User.objects.create_user(username= username, first_name=first_name, last_name=last_name, email=email, password=password)
       user.save()
       messages.success(request, f'You have successfully added {first_name} as one  of your team!!!')
       staff = Staff(user=user, branch= company_branch, role=role, phone=phone, admin=admin)
       staff.save()
       return redirect('staffs')
    

    context = {
        'todays_interactions' : todays_interactions,
        'companys': companys,
        'latest_interactions': latest_interactions,
        'todays_pipelines': todays_pipelines,
        'todays_pipelines_count': todays_pipelines_count,
        'branches': branches
    }
    return render(request, 'add-staff.html', context)

@login_required(login_url="/account/login/")
def pipeline(request):
    user = request.user
    today = date.today()
    
    current_time = datetime.now().time()
    companys = Company.objects.order_by('id')[:1]
    interactions = user.interaction_set.all()
    latest_interactions = interactions.order_by('-id')[:3]
    todays_interactions = interactions.filter(date_created__date=today).count()

    pipelines =Pipeline.objects.filter(created_by=user, done=False, postponed=False, pipeline_date=today)
    all_pipelines = Pipeline.objects.filter(created_by=user, done=False, postponed=False)
    completed = Pipeline.objects.filter(created_by=user, done=True).order_by('-date_updated')
    query = request.GET.get('query')
    search = request.GET.get('search')
    tasks_completed= Pipeline.objects.filter(created_by=user, done=True, pipeline_date=today).count()
    #todays_tasks =  Pipeline.objects.filter(created_by=user, pipeline_date=today, postponed=True).count()
    tasks_postponed=  Pipeline.objects.filter(created_by=user, postponed=True, pipeline_date=today).count()
    tasks_not_completed = Pipeline.objects.filter(created_by=user, done=False, postponed=False, pipeline_date=today).count()
   
    todays_pipelines_count = pipelines.count()
    todays_pipelines = pipelines.order_by('-id')[:3]

    
    if query :
        pipelines = all_pipelines.filter(pipeline_date__icontains=query)
    if search :
        completed = all_pipelines.filter(date_updated__icontains=search)

    if current_time < time(12, 0):
        if todays_pipelines_count == 0 :
            print(current_time)
            messages.success(request, "please add your todays target")
    else:
        if todays_pipelines_count == 0:
            messages.success(request, "please add your todays Report")
    context = {
        'pipelines':pipelines,
        'completed' :completed,
        'query' : query,
        'search': search,
        'tasks_completed' : tasks_completed,
        'tasks_postponed' : tasks_postponed,
        'tasks_not_completed' : tasks_not_completed,

        'todays_interactions' : todays_interactions,
        'companys': companys,
        'latest_interactions': latest_interactions,
        'todays_pipelines': todays_pipelines,
        'todays_pipelines_count': todays_pipelines_count

    }
    return render(request, 'pipeline.html', context)

@login_required(login_url="/account/login/")
def importantPipeline(request):
    user = request.user
    today = date.today()
    companys = Company.objects.order_by('id')[:1]
    interactions = user.interaction_set.all()
    latest_interactions = interactions.order_by('-id')[:3]
    todays_interactions = interactions.filter(date_created__date=today).count()

    pipelines =Pipeline.objects.filter(created_by=user, done=False, postponed=False, pipeline_date=today, important=True)
    all_pipelines = Pipeline.objects.filter(created_by=user, done=False, postponed=False, important=True)
    completed = Pipeline.objects.filter(created_by=user, done=True, important=True).order_by('-date_updated')
    query = request.GET.get('query')
    search = request.GET.get('search')
    tasks_completed= Pipeline.objects.filter(created_by=user, important=True, done=True, pipeline_date=today).count()
    #todays_tasks =  Pipeline.objects.filter(created_by=user, important=True, pipeline_date=today, postponed=True).count()
    tasks_postponed=  Pipeline.objects.filter(created_by=user, postponed=True, important=True, pipeline_date=today).count()
    tasks_not_completed = Pipeline.objects.filter(created_by=user, done=False, important=True, postponed=False, pipeline_date=today).count()

    pipelin =Pipeline.objects.filter(created_by=user, done=False, postponed=False, pipeline_date=today)
    todays_pipelines_count = pipelin.count()
    todays_pipelines = pipelin.order_by('-id')[:3]
    
    
    if query :
        pipelines = all_pipelines.filter(pipeline_date__icontains=query)
    if search :
        completed = all_pipelines.filter(date_updated__icontains=search)

    context = {
        'pipelines':pipelines,
        'completed' :completed,
        'query' : query,
        'search': search,
        'tasks_completed' : tasks_completed,
        'tasks_postponed' : tasks_postponed,
        'tasks_not_completed' : tasks_not_completed,
        'todays_interactions' : todays_interactions,
        'todays_pipelines': todays_pipelines,
        'todays_pipelines_count': todays_pipelines_count,
        'companys': companys,
        'latest_interactions': latest_interactions

    }
    return render(request, 'important-pipeline.html', context)

@login_required(login_url="/account/login/")
def view_pipeline(request, id):
    companys = Company.objects.order_by('id')[:1]
    user = request.user
    today = date.today()
    interactions = user.interaction_set.all()
    latest_interactions = interactions.order_by('-id')[:3]
    todays_interactions = interactions.filter(date_created__date=today).count()

    pipelin =Pipeline.objects.filter(created_by=user, done=False, postponed=False, pipeline_date=today)
    todays_pipelines_count = pipelin.count()
    todays_pipelines = pipelin.order_by('-id')[:3]
    
    pipeline = get_object_or_404(Pipeline, id=id)
    notes = PipelineNotes.objects.filter(pipeline=pipeline).order_by("-id")

    return render(request, 'view_pipeline.html', {
        'pipeline': pipeline,
        'notes' : notes,
        'todays_interactions' : todays_interactions,
        'companys': companys,
        'latest_interactions': latest_interactions,
        'todays_pipelines': todays_pipelines,
        'todays_pipelines_count': todays_pipelines_count
    })

@login_required(login_url="/account/login/")
def addPipelineNotes(request, id):
    if request.method == 'POST':
        notes = request.POST['add-notes']
        instance=get_object_or_404(Pipeline, id=id)

        note = PipelineNotes(pipeline=instance,  notes=notes)
        note.save()
        messages.success(request, "Congradulation!!! You Have Successfully added a note on your task***")
        return redirect('view_pipeline', id=instance.id )

@login_required(login_url="/account/login/")
def edit_pipeline_done(request, id):
  
    if request.method == 'POST':
            completed = request.POST['completedCheckbox'] or False 
            if completed:
                instance=get_object_or_404(Pipeline, id=id)
                print(instance)
                instance.done=True
                instance.save()
                messages.success(request, "Congradulation!!! You Have Successfully Completed the task***")
            return redirect('pipeline')
        #HttpResponsePermanentRedirect('/')

@login_required(login_url="/account/login/") 
def edit_pipeline_resechedule(request, id):
    if request.method == 'POST':
        postponed = request.POST.get('postponed', False)
        new_date =  request.POST['date']
        new_time =  request.POST['time'] or None

        if postponed:
            instance = get_object_or_404(Pipeline, id=id)
            instance.postponed = True
            instance.postponed_counter += int(1)
            instance.save()
            new = Pipeline(task=instance.task, important=instance.important, customer=instance.customer, what_to_expect=instance.what_to_expect, notes=instance.notes, pipeline_date=new_date, pipeline_time=new_time, created_by=instance.created_by, postponed_counter=instance.postponed_counter)
            new.save()
            messages.success(request, "This Task Has Been Postponed;")
            return redirect('view_pipeline', id=instance.id)
    
@login_required(login_url="/account/login/") 
def edit_pipeline(request, id):
  if request.method == 'POST':
        done = request.POST.get('done', False)
        important = request.POST.get('important', False)
        
        instance=get_object_or_404(Pipeline, id=id)
        if done:
            instance.done=True
            messages.success(request, "Congradulation!!! You Have Successfully Completed the task***")
        if important:
            instance.important=True 
            messages.success(request, "You Have Successfully made the task Impoetant***")
        instance.save()
        print('saved')
        return redirect('view_pipeline', id=instance.id)

@login_required(login_url="/account/login/")
def addPipeline(request):
    companys = Company.objects.order_by('id')[:1]
    user = request.user
    today = date.today()
    interactions = user.interaction_set.all()
    latest_interactions = interactions.order_by('-id')[:3]
    todays_interactions = interactions.filter(date_created__date=today).count()

    pipelin =Pipeline.objects.filter(created_by=user, done=False, postponed=False, pipeline_date=today)
    todays_pipelines_count = pipelin.count()
    todays_pipelines = pipelin.order_by('-id')[:3]

    if request.method == 'POST':
        form = AddPipelineForm(request.POST)

        if form.is_valid():
            pipeline = form.save(commit=False)
            pipeline.created_by = request.user
            pipeline.save()
            messages.success(request, "Congradulation!!! You Have Added A New Task!")
            return redirect('view_pipeline', id=pipeline.id)
    else:
        form = AddPipelineForm()
    context = {
        'form' : form,
        'todays_interactions' : todays_interactions,
        'companys': companys,
        'latest_interactions': latest_interactions,
        'todays_pipelines': todays_pipelines,
        'todays_pipelines_count': todays_pipelines_count
    }
    return render(request, 'add-pipeline.html', context)

@login_required(login_url="/account/login/")
def addPipeline(request):
    companys = Company.objects.order_by('id')[:1]
    user = request.user
    today = date.today()
    interactions = user.interaction_set.all()
    latest_interactions = interactions.order_by('-id')[:3]
    todays_interactions = interactions.filter(date_created__date=today).count()

    pipelin =Pipeline.objects.filter(created_by=user, done=False, postponed=False, pipeline_date=today)
    todays_pipelines_count = pipelin.count()
    todays_pipelines = pipelin.order_by('-id')[:3]

    if request.method == 'POST':
        form = AddPipelineForm(request.POST)

        if form.is_valid():
            pipeline = form.save(commit=False)
            pipeline.created_by = request.user
            pipeline.save()
            messages.success(request, "Congradulation!!! You Have Added A New Task!")
            return redirect('view_pipeline', id=pipeline.id)
    else:
        form = AddPipelineForm()
    context = {
        'form' : form,
        'todays_interactions' : todays_interactions,
        'companys': companys,
        'latest_interactions': latest_interactions,
        'todays_pipelines': todays_pipelines,
        'todays_pipelines_count': todays_pipelines_count
    }
    return render(request, 'add-pipeline.html', context)


@login_required(login_url="/account/login/")
def addReport(request):
    companys = Company.objects.order_by('id')[:1]
    user = request.user
    today = date.today()
    interactions = user.interaction_set.all()
    latest_interactions = interactions.order_by('-id')[:3]
    todays_interactions = interactions.filter(date_created__date=today).count()

    pipelin =Pipeline.objects.filter(created_by=user, done=False, postponed=False, pipeline_date=today)
    todays_pipelines_count = pipelin.count()
    todays_pipelines = pipelin.order_by('-id')[:3]

    if request.method == 'POST':
        form = AddReportForm(request.POST, user=user)

        if form.is_valid():
            report = form.save(commit=False)
            report.created_by = request.user
            report.save()
            messages.success(request, f'Congradulation!!! You Have Added A New Report for {report.target.timeline}!')
            return redirect('view_staff', id=request.user.staff.id)
    else:
        form = AddReportForm(user=user)
    context = {
        'form' : form,
        'todays_interactions' : todays_interactions,
        'companys': companys,
        'latest_interactions': latest_interactions,
        'todays_pipelines': todays_pipelines,
        'todays_pipelines_count': todays_pipelines_count
    }
    return render(request, 'add-report.html', context)

@login_required(login_url="/account/login/")
def addTarget(request):
    companys = Company.objects.order_by('id')[:1]
    user = request.user
    today = date.today()
    interactions = user.interaction_set.all()
    latest_interactions = interactions.order_by('-id')[:3]
    todays_interactions = interactions.filter(date_created__date=today).count()

    pipelin =Pipeline.objects.filter(created_by=user, done=False, postponed=False, pipeline_date=today)
    todays_pipelines_count = pipelin.count()
    todays_pipelines = pipelin.order_by('-id')[:3]

    if request.method == 'POST':
        form = AddTargetForm(request.POST)

        if form.is_valid():
            target = form.save(commit=False)
            target.created_by = request.user
            timeline = target.timeline
            # if timeline == 'TODAY':
            #     td= 'Today'
            # if timeline == 'TW':
            #     td= 'This Weeek'
            # if timeline == 'TM':
            #     td= 'This Month'
            # if timeline == 'TY':
            #     td= 'This Year'
            
            target.save()
            messages.success(request, f' You Have Added A New Target for  {timeline}')
            
            return redirect('view_staff', id=request.user.staff.id)
           
    else:
        form = AddTargetForm()
    context = {
        'form' : form,
        'todays_interactions' : todays_interactions,
        'companys': companys,
        'latest_interactions': latest_interactions,
        'todays_pipelines': todays_pipelines,
        'todays_pipelines_count': todays_pipelines_count
    }
    return render(request, 'add-target.html', context)



