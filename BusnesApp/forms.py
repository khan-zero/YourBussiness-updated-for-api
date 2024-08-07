from django import forms
from .models import Portfolio, Member, FAQ

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['img', 'name']

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['full_name', 'position', 'bio', 'profile_picture', 'x_link', 'facebook_link', 'instagram_link', 'linkedin_link']
        
class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['question', 'answer']

