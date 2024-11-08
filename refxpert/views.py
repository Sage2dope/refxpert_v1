from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users, authenticated_user
from django.urls import reverse
from django.db.models import Q
from .forms import *
from .models import *

# Create your views here.
def index(request):
    # Get the latest post from each category
    latest_tenancy_post = BlogPost.objects.filter(category='Tenancy').order_by('-date_created').first()
    latest_legal_post = BlogPost.objects.filter(category='Legal').order_by('-date_created').first()
    latest_landlord_post = BlogPost.objects.filter(category='Landlords').order_by('-date_created').first()

    # Pass the latest posts to the template
    context = {
        'latest_tenancy_post': latest_tenancy_post,
        'latest_legal_post': latest_legal_post,
        'latest_landlord_post': latest_landlord_post,
    }
    return render(request, 'refxpert/index.html', context)

# Registration Page
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    context = {'form': form}
    return render(request, 'refxpert/registration/register.html', context)



#Login Page
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate (request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Account Successfully logged in')
            return redirect('user')
        else:
            messages.info(request, 'Username or Password is incorrect')
    context = {}
    return render(request, 'refxpert/registration/login.html', context)



#Logout Function
@authenticated_user
@login_required(login_url='login')  
def logoutUser(request):
    logout(request)
    messages.success(request, 'Account Successfully logged out')
    return redirect("login")




#User Dashboard Page
@authenticated_user
@login_required(login_url='login')  
def userPage(request):
    user = request.user
    try:
        orders = HouseApplication.objects.filter(user=user)
        total_orders = TenantForm.objects.filter(user=user).count()
        LegalServices = LegalService.objects.filter(user=user)
        total_LegalService = LegalServices.count()
        house_types = orders.values('house_type').distinct().count()
        property = PropertyManagement.objects.filter(user=user)
        total_property = property.count()

        approved = orders.filter(status='Approved').count()
        pending = orders.filter(status='Pending').count()
        rejected = orders.filter(status='Rejected').count()

        context = {"orders": orders,  "total_orders": total_orders, "approved": approved, "pending": pending, "rejected": rejected, "LegalServices": LegalServices, "total_LegalService": total_LegalService, "house_types": house_types, "property": property, "total_property": total_property}
    except TenantForm.DoesNotExist:
        print(f"No TenantForm found for user: {user}")
        context = {"orders": [], "total_orders": 0, "approved": 0, "pending": 0, "rejected": 0, "LegalServices": [], "total_LegalService": 0, "house_types": 0, "property": [], "total_property": 0}

    return render(request, 'refxpert/registration/user.html', context)



#The User Account Profile Page -- will still need to be edited 
@authenticated_user
@login_required(login_url='login')  
def account(request):
    context = {}
    return render(request, 'refxpert/folders/account.html', context)

#Utility portal function 
@authenticated_user
@login_required(login_url='login')  
def utility(request):
    context = {}
    return render(request, 'refxpert/folders/utility.html', context)



#Property Management Function 
@authenticated_user
@login_required(login_url='login')  
def propertymanagement(request): 
    user = request.user
    properties = PropertyManagement.objects.filter(user=user)
    context = {"properties": properties}
    return render(request, 'refxpert/folders/PropertyManagement.html', context)


#Property management view button function
@authenticated_user
@login_required(login_url='login')  
def propertymanagement_view(request, pk):
    property = PropertyManagement.objects.get(id=pk)
    delete_url = reverse('delete_property', args=[pk])
    context = {"property": property, 'delete_url': delete_url}
    return render(request, 'refxpert/folders/propertymanagement_view.html',  context)


#Legal Services Function
@authenticated_user
@login_required(login_url='login')  
def legalservices(request):
    user = request.user
    legalservices = LegalService.objects.filter(user=user)
    context = {"legalservices": legalservices}
    return render(request, 'refxpert/folders/LegalServices.html', context)

#Legal Services view button Function
@authenticated_user
@login_required(login_url='login')  
def legalservices_view(request, pk):
    legalservice = LegalService.objects.get(id=pk)
    delete_url = reverse('delete_service', args=[pk])
    context = {"legalservice": legalservice, 'delete_url': delete_url}
    return render(request, 'refxpert/folders/legalservices_view.html', context)


#My contact form page function
def contact(request):
  
  return render(request, 'refxpert/components/contact.html')



#Career page function 
def careers(request):
    # Fetch all job postings from the database
    jobs = Job.objects.all()

    # Pass the job postings to the template
    context = {'jobs': jobs}
    return render(request, 'refxpert/careers/careers.html', context)


#Application form function
def apply(request, job_id):
    job = get_object_or_404(Job, pk=job_id)

    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            messages.success(request, 'Application Successfully Submitted')
            return redirect('careers')  # replace 'success' with the name of your success view
    else:
        form = ApplicationForm()

    return render(request, 'refxpert/careers/apply.html', {'form': form, 'job': job})


#Job Detail function
def job_detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'refxpert/careers/job_detail.html', {'job': job})


#The tenant reference page where the user - clicks START REFERENCE BUTTON
@authenticated_user
@login_required(login_url='login')  
def tenantref(request):
    search_term = ''

    if 'search' in request.GET:
        search_term = request.GET['search']
        saved_form = TenantForm.objects.filter(
            Q(user=request.user) & (Q(last_name__icontains=search_term) | Q(property_name__icontains=search_term))
        ).order_by('-id')
    else:
        saved_form = TenantForm.objects.filter(user=request.user).order_by('-id')

    context = {'saved_form': saved_form}
    return render(request, 'refxpert/form/tenantref.html', context)



#The tenant reference form page
@authenticated_user
@login_required(login_url='login')  
def tenantform(request):  # sourcery skip: use-contextlib-suppress
    form = TenantForms()
    saved_form = None

    if request.method == 'POST':
        form = TenantForms(request.POST)
        if form.is_valid():
            tenant_form = form.save(commit=False)
            tenant_form.user = request.user
            tenant_form.save()
            saved_form = tenant_form
            messages.success(request, 'Form has been submitted successfully.')
            return redirect('tenantref')
        else:
            messages.error(request, 'Error')
    else:
        try:
            saved_form = TenantForm.objects.filter(user=request.user).latest('id')
        except TenantForm.DoesNotExist:
            pass

        print (saved_form)

    context = {'formz': form, 'saved_form': saved_form}
    return render(request, 'refxpert/form/tenantform.html',context)



#The tenant form view button function
@authenticated_user
@login_required(login_url='login')  
def tenantform_view(request, pk):
    tenantform = TenantForm.objects.get(id=pk)
    delete_url = reverse('delete_tenant', args=[pk])
    context = {"tenants": tenantform, 'delete_url': delete_url}
    return render(request, 'refxpert/form/tenantform_view.html', context)


#The page for handling either to fill the form or send an email link to the tenant to fill the form 
@authenticated_user
@login_required(login_url='login')  
def ref_option(request):
  return render(request, 'refxpert/form/ref_optionform.html')



#Email tenant form 
@authenticated_user
@login_required(login_url='login')  
def email_tenants(request):
  
  return render(request, 'refxpert/form/emailtenant.html')


#delete function of user inputs 
@login_required(login_url='login')
def delete_tenant(request, pk):
    if request.method == 'POST':
        tenant = TenantForm.objects.get(id=pk)
        tenant.delete()
        return redirect('tenantref')
@login_required(login_url='login')
def delete_service(request, pk):
        if request.method == 'POST':
            service = LegalService.objects.get(id=pk)
            service.delete()
            return redirect('legalservices')
@login_required(login_url='login')
def delete_property(request, pk):
        if request.method == 'POST':
            manage = PropertyManagement.objects.get(id=pk)
            manage.delete()
            return redirect('propertymanagement')
        


#Basically my blogpost functions 



def tenancy_post_view(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'refxpert/components/tenancy_post_view.html', {'post': post})

def tenancy_post(request):
    tenancy_posts = BlogPost.objects.filter(category='Tenancy').order_by('-date_created')
    latest_post = tenancy_posts.first() if tenancy_posts else None
    return render(request, 'refxpert/blogpost/tenancy_post.html', {'latest_post': latest_post, 'posts': tenancy_posts[1:]})


def legal_post(request):
    legal_posts = BlogPost.objects.filter(category='Legal').order_by('-date_created')
    latest_post = legal_posts.first() if legal_posts else None
    return render(request, 'refxpert/blogpost/legal_post.html', {'latest_post': latest_post, 'posts': legal_posts[1:]})



def property_post(request):
    property_posts = BlogPost.objects.filter(category='Landlords').order_by('-date_created')
    latest_post = property_posts.first() if property_posts else None
    return render(request, 'refxpert/blogpost/property_post.html', {'latest_post': latest_post, 'posts': property_posts[1:]})



#def test_view(request):
    tenancy_posts = BlogPost.objects.filter(category='Tenancy').order_by('-date_created')
    latest_post = tenancy_posts.first() if tenancy_posts else None
    print(latest_post)  # Add this line
    return render(request, 'refxpert/components/test.html', {'latest_post': latest_post, 'posts': tenancy_posts[1:]})
    