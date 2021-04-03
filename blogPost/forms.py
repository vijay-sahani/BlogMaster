from blogPost.models import BlogPost
from django import forms




ATTRIBUTES={'class':'form-control'}
TEXTAREA={'rows':3}
class AddBlogForm(forms.ModelForm):
        class Meta:
            model=BlogPost
            fields = ['title','user','summary','content','about','image']
            
            widgets={
                'title':forms.TextInput(attrs=ATTRIBUTES),
                'user':forms.TextInput(attrs={'type':'hidden'}),
                'summary':forms.TextInput(attrs=ATTRIBUTES),
                'content':forms.Textarea(attrs={**ATTRIBUTES,**TEXTAREA}),
                'about':forms.Textarea(attrs={**ATTRIBUTES,**TEXTAREA}),
            }

class EditPostForm(forms.ModelForm):
    class Meta:
        model=BlogPost
        fields = ['title','summary','content','about','image']
        widgets={
                'title':forms.TextInput(attrs=ATTRIBUTES),
                'summary':forms.TextInput(attrs=ATTRIBUTES),
                'content':forms.Textarea(attrs={**ATTRIBUTES,**TEXTAREA}),
                'about':forms.Textarea(attrs={**ATTRIBUTES,**TEXTAREA}),
            }
