from mongoengine import Document, StringField, EmailField, SequenceField


class User(Document):
    user_id = SequenceField(primary_key=True)
    email = EmailField(required=True, unique=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)

    def __str__(self):
        return self.email+self.first_name+self.last_name

    def __repr__(self):
        return self.email+self.first_name+self.last_name