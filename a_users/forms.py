from django.forms import ModelForm
from django import forms
from .models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'displayname', 'info']
        widgets = {
            'image': forms.FileInput(attrs={'accept': 'image/jpeg,image/png,image/webp'}),
            'displayname': forms.TextInput(attrs={'placeholder': 'Add display name'}),
            'info': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add information'})
        }

    def clean_image(self):
        image = self.cleaned_data.get('image')

        if image:
            content_type = image.content_type

            allowed_types = ['image/jpeg', 'image/png', 'image/webp']

            if content_type not in allowed_types:
                raise forms.ValidationError(
                    "Only JPG, PNG, or WebP images are allowed.")

             # ✅ File size validation (2MB limit)
            if image.size > 2 * 1024 * 1024:  # 2MB in bytes
                raise forms.ValidationError(
                    "Image size should not exceed 2MB."
                )
        return image
 