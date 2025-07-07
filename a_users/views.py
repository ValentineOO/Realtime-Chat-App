from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_http_methods
from .forms import ProfileForm

# Create your views here.


@require_GET
def profile_view(request):
    profile = request.user.profile
    return render(request, 'a_users/profile.html', {'profile': profile})

@login_required
@require_http_methods(["GET", "POST"])
def profile_edit_view(request):
    form = ProfileForm(instance=request.user.profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES,
                           instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # or your profile view
        else:
            print("🔥 Form errors:", form.errors.as_json())

    return render(request, 'a_users/profile_edit.html', {'form': form})
