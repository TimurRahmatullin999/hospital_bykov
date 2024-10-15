from django.db import models

# Create your models here.


JOB_TITLE = [
    ('tera', 'Терапевт'),
    ('teeth', 'Стоматолог'),
    ('ped', 'Ортопед'),
    ('nev', 'Невролог'),
    ('pshy', 'Психиатр'),
    ('oto', 'Отоларинголог'),
    ('kardio', 'Кардиолог'),
    ('der', 'Дерматолог'),
    ('gen', 'Гинеколог'),
    ('gas', 'Гастроэнтеролог'),
    ('diet', 'Диетолог'),

]

DIAGNOSIS = [
    ('temp', 'Температура'),
    ('cough', 'Кашель'),
    ('rn', 'Насморк'),
    ('highpressure', 'Повышенное давление'),
    ('head', 'Головокружение'),
    ('gas', 'Гастрит'),
    ('ozh', 'Ожирение'),
    ('inf', 'Инфаркт'),
    ('dep', 'Депрессия'),
    ('undef', 'Диагноз не определен'),
    ('gem', 'Геморрой'),
]


class Patient(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=100)
    surname = models.CharField(verbose_name='Фамилия', max_length=100)
    patronymic = models.CharField(verbose_name='Отчество', max_length=100, null=True, blank=True)
    birth_day = models.DateField(verbose_name='Дата рождения')


    class Meta:
        verbose_name='Пациент'
        verbose_name_plural = 'Пациент'
        ordering = ['name', 'surname']


class Manager(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=100)
    surname = models.CharField(verbose_name='Фамилия', max_length=100)
    patronymic = models.CharField(verbose_name='Отчество', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name='Заведующий'
        verbose_name_plural = 'Заведующие'
        ordering = ['name', 'surname']


class Hospitals(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)
    address = models.CharField(verbose_name='Адрес', max_length=100)
    id_manager = models.OneToOneField(
        Manager,
        on_delete=models.CASCADE,
        related_name='idman',
        verbose_name='ID заведующего'
    )

    class Meta:
        verbose_name='Поликлиника'
        verbose_name_plural = 'Поликлиники'
        ordering = ['title', 'adress']


class Doctors(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=100)
    surname = models.CharField(verbose_name='Фамилия', max_length=100)
    patronymic = models.CharField(verbose_name='Отчество', max_length=100, null=True, blank=True)
    job_title = models.CharField(verbose_name='Должность', max_length=100, choices=JOB_TITLE)

    class Meta:
        verbose_name='Доктор'
        verbose_name_plural = 'Доктора'
        ordering = ['name', 'surname']


class Record(models.Model):
    date_time_record = models.DateTimeField(verbose_name='Дата и время записи')
    diagnosis = models.CharField(verbose_name='Диагноз', max_length=100, choices=DIAGNOSIS, null=True, blank=True)
    discription = models.TextField(verbose_name='Описание', null=True, blank=True)
    id_patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='idpat',
        verbose_name='ID пациента'
    )

    id_doctor = models.ForeignKey(
        Doctors,
        on_delete=models.CASCADE,
        related_name='iddoc',
        verbose_name='ID доктора'
    )

    id_hosp = models.ForeignKey(
        Hospitals,
        on_delete=models.CASCADE,
        related_name='idhosp',
        verbose_name='ID поликлиники'
    )

    class Meta:
        verbose_name='Запись'
        verbose_name_plural = 'Записи'
        ordering = ['date_time_record']
