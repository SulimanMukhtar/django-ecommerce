from django.contrib import admin

from apps.products.models import ProductType, ProductSpecification, Product, ProductSpecificationValue, ProductImage

admin.site.register(ProductType)
admin.site.register(ProductSpecification)
admin.site.register(Product)
admin.site.register(ProductSpecificationValue)
admin.site.register(ProductImage)
