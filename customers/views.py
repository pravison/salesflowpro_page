from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import date
from . models import Customer, Note, Interaction, ProbableConversationOutcome, ProbableNextStep, CustomerLabel
from staff.models import Staff, Pipeline
from company.models import Company, Product
from .forms import AddCustomerForm, AddInteractionForm
from django.db.models import  Subquery
# Create your views here.

@login_required(login_url="/account/login/")
def leads(request):
    user = request.user
    today = date.today()

    pipelin =Pipeline.objects.filter(created_by=user, done=False, postponed=False, pipeline_date=today)
    todays_pipelines_count = pipelin.count()
    todays_pipelines = pipelin.order_by('-id')[:3]

    companys = Company.objects.order_by('id')[:1]
    staff = get_object_or_404(Staff, user=user)
    leads = Customer.objects.all().filter(active=False, added_by=user).order_by("-id")
    all_leads = Customer.objects.all().filter(active=False).order_by("-id")
    interactions = user.interaction_set.all()
    latest_interactions = interactions.order_by('-id')[:3]
    todays_interactions = interactions.filter(date_created__date=today).count()

    staff_id = request.GET.get('staff', 0)
    branch_id = request.GET.get('branch', 0)
    company_id = request.GET.get('company', 0)
    query = request.GET.get('query')
    # if query:
    #     leads = all_leads.filter(Q(name__icontains=query)| Q(description__icontains=query) |Q( phone__icontains=query))
   
    if staff_id :
        leads = leads

    if branch_id :
        leads = all_leads.filter(branch__id=branch_id )
    if company_id :
        leads =all_leads

    context={
        'leads': leads,
        'companys': companys,
        'staff': staff, 
        'interactions' : interactions,
        'query' : query,
        'todays_interactions' : todays_interactions,
        'latest_interactions' : latest_interactions,

        'todays_pipelines': todays_pipelines,
        'todays_pipelines_count': todays_pipelines_count,
    }
    return render(request, 'leads.html', context)

@login_required(login_url="/account/login/")
def customers(request):
    user = request.user
    today = date.today()

    pipelin =Pipeline.objects.filter(created_by=user, done=False, postponed=False, pipeline_date=today)
    todays_pipelines_count = pipelin.count()
    todays_pipelines = pipelin.order_by('-id')[:3]

    companys = Company.objects.order_by('id')[:1]
    staff = get_object_or_404(Staff, user=user)
    customers = Customer.objects.all().filter(active=True, added_by=user).order_by("-id")
    all_Customers = Customer.objects.all().filter(active=True).order_by("-id")
    interactions = user.interaction_set.all()
    latest_interactions = interactions.order_by('-id')[:3]
    todays_interactions = interactions.filter(date_created__date=today).count()
    staff_id = request.GET.get('staff', 0)
    branch_id = request.GET.get('branch', 0)
    company_id = request.GET.get('company', 0)
    query = request.GET.get('query')
    # if query:
    #     customers = all_Customers.filter(Q(name__icontains=query)| Q(description__icontains=query) |Q( phone__icontains=query))
   
    if staff_id :
        customers = customers

    if branch_id :
        customers = all_Customers.filter(branch__id=branch_id )

    if company_id :
        customers = all_Customers

    context ={
        'customers': customers,
        'companys': companys,
        'staff': staff, 
        'interactions' : interactions,
        'query': query,
        'todays_interactions' : todays_interactions,
        'latest_interactions' : latest_interactions,

        'todays_pipelines': todays_pipelines,
        'todays_pipelines_count': todays_pipelines_count
    }
    return render(request, 'customers.html', context)

@login_required(login_url="/account/login/")
def viewCustomer(request, id):
    companys = Company.objects.order_by('id')[:1]
    user = request.user
    today = date.today()



    pipelin =Pipeline.objects.filter(created_by=user, done=False, postponed=False, pipeline_date=today)
    todays_pipelines_count = pipelin.count()
    todays_pipelines = pipelin.order_by('-id')[:3]

    interactions = user.interaction_set.all()
    latest_interactions = interactions.order_by('-id')[:3]
    todays_interactions = interactions.filter(date_created__date=today).count()
    customer = get_object_or_404(Customer, id=id)
    notes = Note.objects.all().filter(customer=customer)
    customer_interactions = Interaction.objects.all().filter(customer=customer)
    outcomes =ProbableConversationOutcome.objects.all()
    next_steps = ProbableNextStep.objects.all()

    customr_labels = customer.label.all()
    customer_products = customer.product.all()

    products = Product.objects.exclude(id__in=Subquery(customer_products.values('id')))
    labels = CustomerLabel.objects.exclude(id__in=Subquery(customr_labels.values('id')))
    context={
        'customer': customer,
        'outcomes': outcomes,
        'next_steps': next_steps,
        'notes': notes,
        'todays_interactions' : todays_interactions,
        'customr_labels': customr_labels,
        'customer_products': customer_products,
        'customer_interactions': customer_interactions,
        'companys': companys,
        'latest_interactions': latest_interactions,

        'todays_pipelines': todays_pipelines,
        'todays_pipelines_count': todays_pipelines_count,

        'products': products,
        'labels' :labels
    }
    return render(request, 'view-customer.html', context)

@login_required(login_url="/account/login/") 
def editCustomer(request, id):
  if request.method == 'POST':
        print(request.POST)
        active = request.POST.get('active', False)
        dormant = request.POST.get('dormant', False)
        
        instance=get_object_or_404(Customer, id=id)
        if active:
            instance.active=True
            messages.success(request, "Congradulation!!! You have updated lead to active customer state***")
        if dormant:
            instance.dormant =True 
            messages.success(request, "You have updated customer to dormant state ***")
        instance.save()
        print('saved')
        return redirect('customer', id=instance.id)


@login_required(login_url="/account/login/")
def addCustomerNotes(request, id):
    if request.method == 'POST':
        notes = request.POST['add-notes']
        instance=get_object_or_404(Customer, id=id)

        note = Note(customer=instance, notes=notes, added_by=request.user)
        note.save()
        messages.success(request, "Congradulation!!! You Have Successfully added a note***")
        return redirect('customer', id=instance.id )


@login_required(login_url="/account/login/")
def addCustomer(request):
    companys = Company.objects.order_by('id')[:1]
    user = request.user
    today = date.today()
    interactions = user.interaction_set.all()
    latest_interactions = interactions.order_by('-id')[:3]
    todays_interactions = interactions.filter(date_created__date=today).count()

    pipelin =Pipeline.objects.filter(created_by=user, done=False, postponed=False, pipeline_date=today)
    todays_pipelines_count = pipelin.count()
    todays_pipelines = pipelin.order_by('-id')[:3]

    query = request.GET.get('query')
    if request.method == 'POST':
        form = AddCustomerForm(request.POST)

        if form.is_valid():
            customer = form.save(commit=False)
            customer.added_by = request.user
            # if query != 'customer' :
            #     print(query)
            #     customer.active = False
            # else:
            #     customer.active = True
            customer.save()
            messages.success(request, "Congradulation!!! You Have Added A New Customer !!!")
            return redirect('customer', id=customer.id)
    else:
        form = AddCustomerForm()
    context = {
        'query' : query,
        'form' : form,
        'todays_interactions' : todays_interactions,
        'companys': companys,
        'latest_interactions': latest_interactions,

        'todays_pipelines': todays_pipelines,
        'todays_pipelines_count': todays_pipelines_count
    }
    return render(request, 'add-lead.html', context)

def CustomerSelfAdd(request):
    companys = Company.objects.order_by('id')[:1]
    if request.method == 'POST':
        form = AddCustomerForm(request.POST)

        if form.is_valid():
            customer = form.save(commit=False)
            customer.added_by = request.user
            
            customer.save()
            messages.success(request, "Congradulation*** You Form Has Been Submitted Successfully !!!")
            return redirect('customer_self_add')
    else:
        form = AddCustomerForm()
    context = {
        'form' : form,
        'companys': companys
    }
    return render(request, 'customer-add-self.html', context)

def interactions(request):
    today = date.today()
    user = request.user

    pipelin =Pipeline.objects.filter(created_by=user, done=False, postponed=False, pipeline_date=today)
    todays_pipelines_count = pipelin.count()
    todays_pipelines = pipelin.order_by('-id')[:3]

    interactions_made= user.interaction_set.all()
    latest_interactions = interactions_made.order_by('-id')[:3]
    todays_interactions =  interactions_made.filter(date_created__date=today).count()
    companys = Company.objects.order_by('id')[:1]
    interactions = Interaction.objects.all().filter(staff=user).order_by("-id")
    all_interactions = Interaction.objects.all().order_by("-id")
    staff_id = request.GET.get('staff', 0)
    #branch_id = request.GET.get('branch', 0)
    company_id = request.GET.get('company', 0)
    query = request.GET.get('query')
   
    if staff_id :
        interactions = interactions

    # if branch_id :
    #     interactions = Interaction.objects.all().filter('staff.user.staff.branch.id'==branch_id).order_by("-id")
    if company_id :
        interactions = all_interactions
    context = {
        'companys': companys,
        'interactions': interactions,
        'todays_interactions' : todays_interactions,
        'query' : query,
        'latest_interactions': latest_interactions,

        'todays_pipelines': todays_pipelines,
        'todays_pipelines_count': todays_pipelines_count
    }
    return render(request, 'interactions.html', context)

@login_required(login_url="/account/login/")
def view_interaction(request, id):
    today = date.today()
    user = request.user

    pipelin =Pipeline.objects.filter(created_by=user, done=False, postponed=False, pipeline_date=today)
    todays_pipelines_count = pipelin.count()
    todays_pipelines = pipelin.order_by('-id')[:3]

    interactions_made= user.interaction_set.all()
    latest_interactions = interactions_made.order_by('-id')[:3]
    todays_interactions =  interactions_made.filter(date_created__date=today).count()
    companys = Company.objects.order_by('id')[:1]
    interaction = get_object_or_404(Interaction, id=id)
 
    return render(request, 'view_interaction.html', {
        'interaction' : interaction,
        'todays_interactions' : todays_interactions,
        'companys': companys,
        'latest_interactions': latest_interactions,

        'todays_pipelines': todays_pipelines,
        'todays_pipelines_count': todays_pipelines_count
    })

@login_required(login_url="/account/login/")
def addInteraction(request):
    today = date.today()
    user = request.user

    pipelin =Pipeline.objects.filter(created_by=user, done=False, postponed=False, pipeline_date=today)
    todays_pipelines_count = pipelin.count()
    todays_pipelines = pipelin.order_by('-id')[:3]

    interactions_made= user.interaction_set.all()
    latest_interactions = interactions_made.order_by('-id')[:3]
    todays_interactions =  interactions_made.filter(date_created__date=today).count()
    companys = Company.objects.order_by('id')[:1]
    if request.method == 'POST':
        form =  AddInteractionForm(request.POST)

        if form.is_valid():
            interaction = form.save(commit=False)
            interaction.staff = request.user
            interaction.save()
            note = f"i had {interaction.conversation_method} interaction with {interaction.customer.name} and the outcome was ; a {interaction.outcome.name} . And the  conversation summary was ;  {interaction.conversation_summary}"
            new = Pipeline(task=interaction.next_step.name, customer=interaction.customer, what_to_expect=interaction.what_to_expect, notes=note, pipeline_date=interaction.next_step_date, pipeline_time=interaction.next_step_time, created_by=user)
            new.save()
            messages.success(request, "Congradulation!!! You Have Added A New interaction!")
            return redirect('interactions')
    else:
        form = AddInteractionForm()
    context = {
        'form' : form,
        'todays_interactions' : todays_interactions,
        'companys': companys,
        'latest_interactions': latest_interactions,

        'todays_pipelines': todays_pipelines,
        'todays_pipelines_count': todays_pipelines_count
    }
    return render(request, 'add-interaction.html', context)


@login_required(login_url="/account/login/")
def addCustomerInteraction(request, id):
    if request.method == 'POST':
        conversation_method = request.POST['conversation_method']
        outcome_id = request.POST['outcome']
        conversation_summary = request.POST['conversation_summary']
        next_step_id = request.POST['next_step']
        what_to_expect = request.POST['what_to_expect']
        next_step_date = request.POST['next_step_date']
        next_step_time = request.POST['next_step_time']
        customer = get_object_or_404(Customer, id=id)
        staff = request.user
        next_step = get_object_or_404(ProbableNextStep, id=outcome_id)
        outcome = get_object_or_404(ProbableConversationOutcome, id=next_step_id)

        interaction = Interaction(customer=customer,  staff=staff, conversation_method=conversation_method, outcome=outcome, conversation_summary=conversation_summary, next_step=next_step, what_to_expect=what_to_expect, next_step_date=next_step_date, next_step_time=next_step_time)
        interaction.save()
        note = f"i had {conversation_method} interaction with {customer.name} and the outcome was ; a {outcome.name} . And the  conversation summary was ;  {conversation_summary}"
        new = Pipeline(task=next_step.name, customer=customer, what_to_expect=what_to_expect, notes=note, pipeline_date=next_step_date, pipeline_time=next_step_time, created_by=staff)
        new.save()
        messages.success(request, "Congradulation!!! You Have Successfully added an interaction to your customer ***")
        return redirect('customer', id=id )


@login_required(login_url="/account/login/")
def addProduct(request, id ):
    if request.method == 'POST':
       product_name = request.POST['product_name']
       product_price = request.POST['product_price'] or 0
       product = Product.objects.create(product_name= product_name, product_price=product_price)
       product.save()
       messages.success(request, f'You have successfully added {product_name} as anew product !!!')
       return redirect('customer', id=id )
    
@login_required(login_url="/account/login/")
def addCustomerProduct(request, id ):
    customer = get_object_or_404(Customer, id=id )
    if request.method == 'POST':
       product_id = request.POST['product']
       customer_product = get_object_or_404(Product, id=product_id)

       customer.product.add(customer_product)
       messages.success(request, f'You have successfully added this {customer_product.product_name} to {customer.name} !!!')
       return redirect('customer', id=id )
    
@login_required(login_url="/account/login/")
def addLabel(request, id ):
    if request.method == 'POST':
       label = request.POST['label']
       definition = request.POST['definition']
       colour = request.POST['colour']
       labelObject = CustomerLabel.objects.create(label=label,  colour= colour, definition=definition)
       labelObject.save()
       messages.success(request, f'You have successfully added {label} as anew label !!!')
       return redirect('customer', id=id )
    
@login_required(login_url="/account/login/")
def addCustomerLabel(request, id ):
    customer = get_object_or_404(Customer, id=id )
    if request.method == 'POST':
       label_id = request.POST['label']
       customer_label = get_object_or_404(CustomerLabel, id=label_id)

       customer.label.add(customer_label)
       messages.success(request, f'You have successfully added this {customer_label.label} to {customer.name} !!!')
       return redirect('customer', id=id )