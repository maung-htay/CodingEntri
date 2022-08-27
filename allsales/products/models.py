from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200, null=False)
    content = models.TextField(max_length=500, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.title

    @property
    def sale_price(self):
        return "%.2f" % (float(self.price) * 0.8)
        # return '' + self.price * 0.8

    @property
    def get_discount(self):
        obj = {
            'id': self.id,
            'title': self.title
        }
        return obj
