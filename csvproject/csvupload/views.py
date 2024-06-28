from django.shortcuts import render
from .forms import CSVUploadForm
import csv
from django.contrib import messages
import mysql.connector


def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']
            csv_data = handle_uploaded_file(csv_file)
            messages.success(request, 'File uploaded and processed successfully')
            return render(request, 'csvupload/upload_csv.html', {'form': form, 'csv_data': csv_data})
        else:
            messages.error(request, 'Failed to upload file')
    else:
        form = CSVUploadForm()
    return render(request, 'csvupload/upload_csv.html', {'form': form})


def handle_uploaded_file(csv_file):
    csv_data = []
    try:
        # Decode the uploaded file using UTF-8 encoding
        file_data = csv_file.read().decode('utf-8')
        # Split the file content by newline character to get rows
        rows = file_data.split('\n')
        # Iterate over rows and append non-empty rows to csv_data
        for row in rows:
            if row.strip():
                # Split row by comma to get columns
                columns = row.split(',')
                # Append columns to csv_data
                # print(columns[0])
                csv_data.append(columns)
    except Exception as e:
        # Handle any errors that might occur during file processing
        print("Error processing CSV file:", e)
        return []
    return csv_data


def getdata():
    mydb = mysql.connector.connect(
        host="localhost",
        user="myusername",
        password="mypassword",
        database="mydatabase"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT id FROM users WHERE display_name!='' AND avatar_url!='' ORDER BY RAND() LIMIT 1")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

def index(request):
    return render(request, 'csvupload/index.html')


