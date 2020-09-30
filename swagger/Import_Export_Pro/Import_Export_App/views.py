


from django.shortcuts import render
from django.http import HttpResponse
from .resources import PersonResource


def export_json(request):
    person_resource = PersonResource()

    dataset = person_resource.export()

    response = HttpResponse(dataset.json, content_type='application/json')

    response['Content-Disposition'] = 'attachment; filename="persons.json"'
    return response




def export_excel(request):
    person_resource = PersonResource()
    dataset = person_resource.export()

    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response



def export_csv(request):
    person_resource = PersonResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="persons.csv"'
    return response








from tablib import Dataset

def simple_upload(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()

        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())

        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():

            person_resource.import_data(dataset, dry_run=False)  # Actually import now
        else:
            return HttpResponse('Data not imported into db')

    # return render(request, 'core/simple_upload.html')
    return render(request, 'import.html')











# from tablib import Dataset
#
# def simple_upload(request):
#     if request.method == 'POST':
#         print('h1')
#
#         person_resource = PersonResource()
#
#         print('h2')
#
#         new_persons = request.FILES['myfile']
#         print('h3')
#
#         dataset = Dataset()
#         try:
#             dataset.load(new_persons.read())
#             print('h4')
#         except:
#             return HttpResponse('Invalid dimentions')
#         else:
#             print('h51')
#             result = person_resource.import_data(dataset, dry_run=True)  # Test the data import
#             print('h5')
#             print(result.rows)
#
#             if not result.has_errors():
#                 print('h6')
#                 person_resource.import_data(dataset, dry_run=False)  # Actually import now
#                 print('h7')
#                 return HttpResponse('Data saved successfully.')
#             else:
#                 print('h8')
#                 return HttpResponse('Please send valid data.')
#     else:
#         return render(request, 'import.html')

