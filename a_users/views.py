from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm

# Create your views here.


def profile_view(request):
    profile = request.user.profile
    return render(request, 'a_users/profile.html', {'profile': profile})


@login_required
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

        # if form.is_valid():
        #     form.save()
        #     return redirect('profile')

    return render(request, 'a_users/profile_edit.html', {'form': form})


# @require_http_methods(["GET", "POST"])
# @login_required
# def profile_edit_view(request):
#     profile = request.user.profile

#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')  # replace with your profile view name
#         else:
#             print("🔥 Form Errors:", form.errors)  # Debug here
#     else:
#         form = ProfileForm(instance=profile)

#     return render(request, 'a_users/profile_edit.html', {'form': form})
