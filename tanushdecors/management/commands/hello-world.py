from django.core.management.base import BaseCommand
from tanushdecors.models import Product

class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument("ids", nargs="+", type=int)

    def handle(self, *args, **options):
        products = Product.objects.all()

        print('List of products')
        for product in products:
            print(product.name, product.category, product.price, product.image)