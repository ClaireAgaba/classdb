from django.db import models

# Create your models here.


class Branch(models.Model):
    branch_number = models.CharField(max_length=5, primary_key=True)
    branch_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    tel_no = models.CharField(max_length=15)


    def __str__(self) :
        return self.branch_name

class Staff(models.Model):
    staff_number = models.CharField(max_length=5, primary_key=True)
    branch_number= models.ForeignKey(Branch, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self) :
        return self.name

class Member(models.Model):
    member_number = models.CharField(max_length=5, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
    registration_date = models.DateField()
    branch_number = models.ForeignKey(Branch, on_delete=models.CASCADE)


    def __str__(self) :
        return self.first_name + " " + self.last_name


class Video(models.Model):
    catalog_number = models.CharField(max_length=10, primary_key=True)
    video_number = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    daily_rental = models.DecimalField(max_digits=10, decimal_places=2)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    status = models.CharField(max_length=50)
    actors = models.TextField()
    director = models.CharField(max_length=100)
    year = models.DateField()


    def __str__(self) :
        return self.title + " " + self.catalog_number
    

class Rental(models.Model):
    rental_number = models.CharField(max_length=5, primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    rental_date = models.DateField()
    return_date = models.DateField()
    due_date = models.DateField()

    def __str__(self) :
        return self.rental_number