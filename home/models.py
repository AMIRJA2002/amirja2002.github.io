from django.db import models


class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')


class ExcelData(models.Model):
    row = models.CharField(max_length=500, null=True, blank=True)
    engine_power = models.CharField(max_length=500, null=True, blank=True)
    engine_serial_number = models.CharField(max_length=500, null=True, blank=True)
    floor = models.CharField(max_length=500, null=True, blank=True)
    pump_type = models.CharField(max_length=500, null=True, blank=True)
    pump_specifications = models.CharField(max_length=500, null=True, blank=True)
    city_of_origin = models.CharField(max_length=500, null=True, blank=True)
    manufacturer = models.CharField(max_length=500, null=True, blank=True)
    code = models.CharField(max_length=500, null=True, blank=True)
    serial_number = models.CharField(max_length=500, null=True, blank=True)



    def __str__(self):
        return f'{self.row}'


class Pump(models.Model):
    class Status(models.TextChoices):
        UNDER_REPAIR = 'در حال تعمیر', 'در حال تعمیر'
        REPAIRED = 'تعمیر شده', 'تعمیر شده'

    code = models.IntegerField(verbose_name='کد')
    engine_power = models.OneToOneField('EnginKind', related_name='pump', on_delete=models.CASCADE, verbose_name='قدرت موتور')
    pump_model = models.OneToOneField('PumpModel', related_name='pump', on_delete=models.CASCADE, verbose_name='مدل پمپ')
    serial_number = models.IntegerField(verbose_name='شماره سریال')
    origin_city = models.OneToOneField('OriginCity', related_name='origin_city', on_delete=models.CASCADE, verbose_name='شهر مبدا', null=True, blank=True)
    destination_city = models.OneToOneField('DestinationCity', related_name='destination_city', on_delete=models.CASCADE, verbose_name='شهر مقصد', null=True, blank=True)
    builder_company = models.OneToOneField('BuilderCompany', related_name='builder_company', on_delete=models.CASCADE, verbose_name='کمپانی سازنده')
    date = models.DateField(verbose_name='تاریخ')
    courier = models.CharField(max_length=300, verbose_name='مامور تحویل')
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.REPAIRED, verbose_name='وضعیت')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ('پمپ')
        verbose_name_plural = ('پمپ')

    def __str__(self):
        return f'{self.code}'


class EnginKind(models.Model):
    kind = models.CharField(max_length=50, verbose_name='نوع')

    class Meta:
        verbose_name = ('قدرت موتور')
        verbose_name_plural = ('قدرت موتور')

    def __str__(self):
        return self.kind


class PumpModel(models.Model):
    model = models.CharField(max_length=100, verbose_name='مدل')

    class Meta:
        verbose_name = ('مدل پمپ')
        verbose_name_plural = ('مدل پمپ')

    def __str__(self):
        return self.model


class OriginCity(models.Model):
    name = models.CharField(max_length=150, verbose_name='اسم')

    class Meta:
        verbose_name = ('شهر مبدا')
        verbose_name_plural = ('شهر مبدا')

    def __str__(self):
        return self.name


class DestinationCity(models.Model):
    name = models.CharField(max_length=200, verbose_name='اسم')

    class Meta:
        verbose_name = ('شهر مقصد')
        verbose_name_plural = ('شهر مقصد')

    def __str__(self):
        return self.name


class BuilderCompany(models.Model):
    name = models.CharField(max_length=300, verbose_name='اسم')

    class Meta:
        verbose_name = ('شرکت سازنده')
        verbose_name_plural = ('شرکت سازنده')

    def __str__(self):
        return self.name

