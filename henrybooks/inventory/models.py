from django.db import models

class Book(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail_url = models.URLField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title

class Branch(models.Model):
    branch_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.branch_name

class Inventory(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        unique_together = ('book', 'branch')

    def __str__(self):
        return f"{self.book.title} @ {self.branch.branch_name} ({self.quantity})"
