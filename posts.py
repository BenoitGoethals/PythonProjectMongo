from mongoengine import Document, StringField, DictField, ListField, DateTimeField, EmbeddedDocument, \
    EmbeddedDocumentField, ObjectIdField, SequenceField

POST_STATUS = ('pending', 'published', 'deleted', 'draft', )


class PostMetatag(EmbeddedDocument):
    title = StringField()
    description = StringField()
    encode = StringField(default='utf-8')


class PostCategory(EmbeddedDocument):
    id = ObjectIdField()
    title = StringField()


class Posts(Document):
    post_id = SequenceField()
    title =StringField(db_field='blog-title-test')
    url = StringField()
    content = StringField()
    metatag = EmbeddedDocumentField(PostMetatag)
    categorys = ListField(EmbeddedDocumentField(PostCategory))
    authors = ListField(ObjectIdField())
    status = StringField(choices=POST_STATUS)
    updated_at = DateTimeField()
    created_at = DateTimeField()

    meta = {
        'auto_create_index': True,
        'index_background': True,
        'indexes': [{
            'name': 'status',
            'fields': ('status', 'created_at', )
        }, {
            'name': 'url',
            'fields': ('url', ),
            'unique': True
        }]
    }