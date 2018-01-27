from django import forms


from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "first_name",
            "last_name",
            "street",
            "street_nr",
            "post_code",
            "city",
            "land",
            "phone_nr",
        ]
