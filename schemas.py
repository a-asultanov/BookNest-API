from extensions import ma

class BookSchema(ma.Schema):    
    class Meta:
        fields = ("id", "title", "author", "genre", "is_read")