from django.http import HttpResponse
from django.shortcuts import render, redirect

from django import forms
from django.views.decorators.csrf import csrf_exempt

from .models import Problem


class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ('name', 'phone', 'address', 'gav', 'problem')
        labels = {
            'name': 'नाम',
            'phone': 'फ़ोन',
            'address': 'पता',
            'gav': 'गांव',
            'problem': 'समस्या',
        }
        widgets = {
            'phone': forms.NumberInput(),
            'problem': forms.Textarea(attrs={"rows": 4})
        }

    def __init__(self, *args, **kwargs):
        super(ProblemForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'


@csrf_exempt
def home(request):
    if request.method == 'POST':
        form = ProblemForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>आपकी समश्या के निवारण के लिए आपके पास जल्द ही फ़ोन आएगा.</h1>")
    else:
        form = ProblemForm()
    return render(request, 'home.html', {'form': form})

