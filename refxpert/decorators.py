from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.shortcuts import redirect, render

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.is_authenticated:
                if request.user.groups.exists():
                    groups = request.user.groups.all()
                    for group in groups:
                        if group.name in allowed_roles:
                            return view_func(request, *args, **kwargs)
                return redirect('login')
                 
            else:
                return redirect('login')
        return wrapper_func
    return decorator





def authenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func