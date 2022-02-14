from .models import Book
from import_export import fields, resources

class BookResource(resources.ModelResource):
    author = fields.Field(
        column_name='Author'
    )

    created = fields.Field(
        column_name='Created'
    )

    id = fields.Field(
        column_name='ID',
        attribute='id'
    )

    title = fields.Field(
        column_name='Title',
        attribute='title'
    )
  
    publish_status = fields.Field(
        column_name='Status',
        attribute='publish_status'
    )
 
    
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'publish_status', 'created')
        export_order = ('id', 'title', 'author', 'publish_status', 'created')

    def dehydrate_author(self, obj):
        return obj.author.name
        
    def dehydrate_created(self, obj):
        return obj.created.strftime("%d-%m-%y")