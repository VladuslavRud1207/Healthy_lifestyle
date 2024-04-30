from django.db import models
from datetime import date
# Create your models here.

class r1(models.Model):
    Ім_я = models.CharField(max_length=50)
    Прізвище = models.CharField(max_length=50)
    Дата_народження = models.DateField()
    Стать = models.CharField(max_length=10)
    Електронна_пошта = models.CharField(max_length=100)
    Місце_проживання = models.CharField(max_length=100, default='Unknown')
    Ціль = models.TextField()

        # Додайте інші записи за необхідністю
class r2(models.Model):
    Опис_цілі = models.TextField()
    Дата_початку = models.DateField()
    Дата_завершення = models.DateField()

class r3(models.Model):
    Опис_цілі = models.TextField()
    Тип_цілі = models.CharField(max_length=50)
    Зріст = models.DecimalField(max_digits=5, decimal_places=2)
    Вага = models.DecimalField(max_digits=5, decimal_places=2)


class r4(models.Model):
    Дата_початку = models.DateField()
    Дата_завершення = models.DateField()
    Статус = models.CharField(max_length=50)

class r5(models.Model):
    Зріст = models.DecimalField(max_digits=5, decimal_places=2)
    Вага = models.DecimalField(max_digits=5, decimal_places=2)
    Кров_яний_тиск = models.CharField(max_length=20)
    Відсоток_жиру_в_тілі = models.DecimalField(max_digits=5, decimal_places=2)
    Рівень_холестерину = models.CharField(max_length=20)
    Індекс_маси_тіла = models.DecimalField(max_digits=5, decimal_places=2)
    Тип_активності = models.CharField(max_length=100)
    Дата_проведення_активності = models.DateField()

class r6(models.Model):
    Тип_активності = models.CharField(max_length=100)
    Тривалість = models.DurationField()
    Дата_проведення_активності = models.DateField()
    Кількість_разів_на_тиждень = models.IntegerField()
    Тренування = models.CharField(max_length=100, default='Unknown')
class r7(models.Model):
    Тип_активності = models.CharField(max_length=100)
    Тривалість = models.DurationField()
    Кількість_спалених_калорій = models.IntegerField()

class r8(models.Model):
    Назва_тренування = models.CharField(max_length=100)
    Опис_тренування = models.TextField()
    Домінуюча_група_м_язів = models.CharField(max_length=100)
    Кількість_повторів = models.IntegerField()
    Кількість_підходів = models.IntegerField()
    Необхідне_обладнання = models.TextField()
    Кількість_калорій = models.IntegerField()
    Вміст_білків = models.DecimalField(max_digits=5, decimal_places=2)

class r9(models.Model):
    Кількість_повторів = models.IntegerField()
    Кількість_підходів = models.IntegerField()
    Рівень_складності = models.CharField(max_length=50)

class r10(models.Model):
    Кількість_калорій = models.IntegerField()
    Вміст_білків = models.DecimalField(max_digits=5, decimal_places=2)
    Вміст_жирів = models.DecimalField(max_digits=5, decimal_places=2)
    Вміст_вуглеводів = models.DecimalField(max_digits=5, decimal_places=2)
    Вміст_клітковини = models.DecimalField(max_digits=5, decimal_places=2)
    Дата = models.DateField()
    Настрій = models.CharField(max_length=50)


class r11(models.Model):
    Дата = models.DateField()
    Настрій = models.CharField(max_length=50)
    Рівень_енергії = models.CharField(max_length=50)
    Симптом = models.TextField()
    Дата_сну = models.DateField()
    Час_засинання = models.TimeField()
    Час_пробудження = models.TimeField()

class r12(models.Model):
    Симптом = models.TextField()
    Прийняті_ліки = models.TextField()

class r13(models.Model):
    Дата_сну = models.DateField()
    Час_засинання = models.TimeField()
    Час_пробудження = models.TimeField()
    Тривалість_сну = models.DurationField()
    Ім_я = models.CharField(max_length=50)
    Прізвище = models.CharField(max_length=50)

class r14(models.Model):
    Тривалість_сну = models.DurationField()
    Якість_сну = models.CharField(max_length=50)

