
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from . forms import InputForm
import aws_redaction_v1 as redact

def index(request):
    form = InputForm()
    return render(request,'index.html',context = {'form':form})

def get_text(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = InputForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            redacted_text = redact.Redact(form.cleaned_data['input_text'],.15)
            return render(request, 'index.html',{'form':form,'redacted_text':redacted_text})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = InputForm()
        return render(request, 'index.html', {'form': form})
