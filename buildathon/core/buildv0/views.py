from django.shortcuts import render
from django.http import HttpResponse
from .forms import DocumentForm
from .models import *
import pandas as pd

# Create your views here.

def home(request):
    if request.method=="POST":
        
        # form = DocumentForm(request.FILES)
        uploaded_file = request.FILES.get('file')
        #Document.objects.create(document=uploaded_file)
        print("wowddddddddddddd")
                    # Process the Excel file using pandas
        df = pd.read_excel(uploaded_file)
        columns = df.columns.tolist()
        #print(df)
        df = df.drop(columns=['marks'])
        #print(df)
            # Get the number of rows and columns
        num_rows = df.shape[0]
        num_columns =df.shape [1]
        context = {'datacolumns':columns}
            # Do something with the DataFrame (e.g., print or save to database)
        #print(f'Number of rows: {num_rows}')
        #print(f'Number of columns: {num_columns}')

        return render(request,'index.html',context)

    return render(request,'index.html')

def create(request):
    print("hola amigo")
    if request.method =="POST":
        uploaded_file = request.FILES.get('file')
        print(type(uploaded_file))
        df = pd.read_excel(uploaded_file)

            # Get the number of rows and columns
        num_rows = df.shape[0]
        num_columns = df.shape[1]

            # Do something with the DataFrame (e.g., print or save to database)
        print(f'Number of rows: {num_rows}')
        print(f'Number of columns: {num_columns}')
        success = "uploaded succefully"
        return HttpResponse(success)
