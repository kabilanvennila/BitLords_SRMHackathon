from django.shortcuts import render,HttpResponseRedirect
from . import summarizer
# Create your views here.


def my_file(request):
    if request.method == 'POST':
        fl = request.FILES['myfile'] 
    # doc_name = doc['filename']
    # fl=request.FILES['myfile']
        if fl:
            su=summarizer.convert_pdf_to_txt(fl)
            return render(request,'researchpalapp/summary.html',context={'summ':su})

    return render(request,'researchpalapp/file.html')

def home(request):
    return render(request,'researchpalapp/home.html')