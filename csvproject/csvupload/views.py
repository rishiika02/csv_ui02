from django.shortcuts import render, redirect
from .forms import CSVUploadForm
from .models import CSVFile
import csv
from django.contrib import messages
from io import TextIOWrapper

def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            handle_uploaded_file(request.FILES['file'])
            messages.success(request, 'File uploaded and processed successfully')
            return redirect('upload_csv')
    else:
        form = CSVUploadForm()
    return render(request, 'csvupload/upload_csv.html', {'form': form})

def handle_uploaded_file(file):
    # Read the file from the InMemoryUploadedFile object
    file_data = TextIOWrapper(file, encoding='utf-8')
    reader = csv.reader(file_data)
    for row in reader:
        # Process each row
        print(row)

def index(request):
    return render(request, 'csvupload/index.html')
