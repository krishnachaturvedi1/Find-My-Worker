from django.shortcuts import render, get_object_or_404
from .forms import PincodeSearchForm
from worker.models import Worker

# Create your views here.

def search_workers(request):
    form = PincodeSearchForm()
    workers = None
    message = ""
    if request.method == 'POST':
        form = PincodeSearchForm(request.POST)
        if form.is_valid():
            pincode = form.cleaned_data['pincode']
            workers = Worker.objects.filter(pin_code=pincode)
            if not workers:
                message = "No workers found for the entered pincode."
    return render(request, 'search_workers.html', {'form': form, 'workers': workers, 'message': message})

def worker_dashboard(request, worker_id):
    worker = get_object_or_404(Worker, id=worker_id)
    return render(request, 'worker_dashboard.html', {'worker': worker})