from django.db import models


class Client(models.Model):
    company_name = models.CharField('Название компании', max_length=250)
    address = models.CharField('Адрес', max_length=250)
    INN = models.CharField('ИНН', max_length=250)
    r_score = models.CharField('р/с', max_length=250)
    BIC = models.CharField('БИК', max_length=250)
    name_manager = models.CharField('ФИО', max_length=250)
    contact_person = models.CharField('ФИО контактного лица', max_length=250)
    tel_contact_person = models.CharField('телефон контактного лица', max_length=250)
    mail = models.CharField('e-mail', max_length=250)
    password = models.CharField('пароль', max_length=250)
    client_code = models.CharField('код клиента', max_length=250)

    def __str__(self):
        return f'{self.company_name} - {self.address} - {self.INN} - {self.r_score} - {self.BIC} - {self.name_manager} - {self.contact_person} - {self.tel_contact_person} - {self.mail} - {self.password} - {self.client_code}'

    class Meta:
        verbose_name = "Клиент ЮЛ"
        verbose_name_plural = "Клиенты ЮЛ"


class ClientFL(models.Model):
    FIO = models.CharField('ФИО', max_length=250)
    client_code = models.CharField('код клиента', max_length=250)
    passport_data = models.CharField('Паспортные данные', max_length=250)
    Date_of_birth = models.CharField('Дата рождения', max_length=250)
    address = models.CharField('Адрес', max_length=250)
    mail = models.CharField('e-mail', max_length=250)
    password = models.CharField('пароль', max_length=250)


    def __str__(self):
        return f'{self.FIO} - {self.client_code} - {self.passport_data} - {self.Date_of_birth} - {self.address} - {self.mail} - {self.password}'

    class Meta:
        verbose_name = "Клиент ФЛ"
        verbose_name_plural = "Клиенты ФЛ"


class Employee(models.Model):
    cod_employee = models.CharField('Код сотрудника', max_length=250)
    post = models.CharField('Должность', max_length=250)
    FIO = models.CharField('ФИО', max_length=250)
    login = models.CharField('Логин', max_length=250)
    password = models.CharField('пароль', max_length=250)
    orders = models.CharField('Заказы', max_length=250, blank=True)

    def __str__(self):
        return f'{self.cod_employee} - {self.post} - {self.FIO} - {self.login} - {self.password} - {self.orders}'

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"


class Product(models.Model):
    index = models.CharField('ID', max_length=250, blank=True)
    product = models.CharField('Наименование товара', max_length=250)
    art = models.CharField('Артикул', max_length=250)
    price = models.CharField('Цена', max_length=250)

    def __str__(self):
        return f'{self.product} - {self.art} - {self.price}'

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Order(models.Model):
    index = models.CharField('ID', max_length=250, blank=True)
    order_number = models.CharField('Номер заказа', max_length=250)
    date_creation = models.CharField('Дата создания', max_length=250)
    client_code = models.CharField('Код клиента', max_length=250)
    article = models.CharField('Артиикул', max_length=250)
    status = models.CharField('Статус', max_length=250)
    closing_date = models.CharField('Дата закрытия', max_length=250, blank=True)
    employee_code = models.CharField('Код сотрудника', max_length=250)

    def __str__(self):
        return f'{self.order_number} - {self.date_creation} - {self.client_code} - {self.article} - {self.status} - {self.closing_date} - {self.employee_code}'

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
