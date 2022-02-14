from django.contrib import admin
from .models import Author, Book
from import_export import resources
from import_export.admin import ExportActionMixin, ImportExportActionModelAdmin
from import_export.fields import Field

class BookResource(resources.ModelResource):
    author = Field()
    created = Field()
    
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'publish_status', 'created')
        export_order = ('id', 'title', 'author', 'publish_status', 'created')

    def dehydrate_author(self, obj):
        return obj.author.name
        
    def dehydrate_created(self, obj):
        return obj.created.strftime("%d-%m-%y")
        

class BookAdmin(ImportExportActionModelAdmin):
    resource_class = BookResource


admin.site.register(Author)
admin.site.register(Book, BookAdmin)