# excel_reader/views.py

from django.shortcuts import render
from .forms import UploadFileForm
from .models import UploadedFile, ExcelData, PumpModel
import openpyxl
import json
from string import ascii_letters

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['file']
            instance = UploadedFile(file=uploaded_file)
            instance.save()

            # Process the uploaded file (read rows and columns)
            workbook = openpyxl.load_workbook(instance.file.path)
            sheet = workbook.active
            data = []

            # Iterate through all rows and columns
            for row in sheet.iter_rows(min_row=2, values_only=True):
                    a = row[0]
                    if isinstance(a, int):
                        row_data = {
                            'ردیف': row[0],
                            'قدرت موتور (KW)': row[1],
                            'شماره سریال موتور': row[2],
                            'طبقه': row[3],
                            'نوع پمپ': row[4],
                            'مشخصات پمپ': row[5],
                            'شهرستان مبدأ': row[6],
                            'شرکت سازنده': row[7],
                            'کد': row[8],
                            'شماره سریال': row[9],
                        }
                        ExcelData.objects.create(row=row_data['ردیف'], engine_power=row_data['قدرت موتور (KW)'], engine_serial_number=row_data['شماره سریال موتور'], floor=row_data['طبقه'], pump_type=row_data['نوع پمپ'], pump_specifications=row_data['مشخصات پمپ'], city_of_origin=row_data['شهرستان مبدأ'], manufacturer=row_data['شرکت سازنده'], code=row_data['کد'], serial_number=row_data['شماره سریال'])
                        data.append(row_data)
                    else:
                        pass
            # Convert data to JSON
            json_data = json.dumps(data, ensure_ascii=False)

            context = {'json_data': json_data}
            print(context)
            return render(request, 'excel_reader/display_json.html', context)
    else:
        form = UploadFileForm()

    return render(request, 'excel_reader/upload_file.html', {'form': form})



def display_data(request):
    data_objects = ExcelData.objects.all()
    print(data_objects)
    return render(request, 'base_generic.html', {'data_objects': data_objects})


def tesete(request):
    for i in range(1, 31):
        a = f'435.{i}'
        PumpModel.objects.create(model=a)



