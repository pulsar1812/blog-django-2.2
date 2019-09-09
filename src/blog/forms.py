"""
Form for a blog post
"""
from django import forms

from .models import BlogPost


class BlogPostForm(forms.Form):
    """Blog post form"""

    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)


class BlogPostModelForm(forms.ModelForm):
    """Blog post model form"""

    class Meta:
        model = BlogPost
        fields = ["title", "slug", "content"]

    def clean_title(self, *args, **kwargs):
        """Return a cleaned title"""
        instance = self.instance
        title = self.cleaned_data.get("title")
        qs = BlogPost.objects.filter(title__iexact=title)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError(
                "This title has already been used. Please input again."
            )
        return title
