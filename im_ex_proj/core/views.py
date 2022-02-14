from django.http import HttpResponse
from django.shortcuts import render
from django.template import context
from .models import Book
from django.http import HttpResponse
from .resources import BookResource
from .forms import NewForm
from django.template.loader import get_template
from weasyprint import HTML


def PostList(request):
    queryset = Book.objects.all()
    form = NewForm()
    context = {'obj': queryset, 'form':form}

    if request.method=='POST':
        form = NewForm(request.POST)
        if form.is_valid():
            dataFormat = (form.cleaned_data['category'])

            # If User Selects CSV Format
            if dataFormat == 'csv':
                book_resource = BookResource()
                dataset = book_resource.export()
                response = HttpResponse(dataset.csv, content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename="books.csv"'
                return response

            # If User Selects XLS Format
            elif dataFormat == 'xls':
                book_resource = BookResource()
                dataset = book_resource.export()
                response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
                response['Content-Disposition'] = 'attachment; filename="books.xls"'
                return response

            # If User Selects JSON Format   
            elif dataFormat == 'json':
                book_resource = BookResource()
                dataset = book_resource.export()
                response = HttpResponse(dataset.json, content_type='application/json')
                response['Content-Disposition'] = 'attachment; filename="books.json"'
                return response

            # If User Selects PDF Format   
            elif dataFormat == 'pdf':
                # obj = Book.objects.all()
                template = get_template('core/pdf-output.html')
                html = template.render(context)
                response = HttpResponse(content_type='application/pdf')
                result = HTML(string=html).write_pdf(response)
                response['Content-Disposition'] = 'attachment; filename="books.pdf"'
                response['Content-Transfer-Encoding'] = 'binary'
                return response
        else:
            print('Form Is Invalid')
    else:
        form = NewForm()
    return render(request, 'core/postlist.html', context)
    
