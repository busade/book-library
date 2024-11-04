from .utils import db



class Books(db.Model):
    __tablename__ = "books"
    id= db.Column(db.Integer(), primary_key = True)
    title = db.Column(db.String(), nullable = False)
    author = db.Column(db.String(100), nullable = False)
    genre = db.Column (db.String(), nullable = False)
    publication_date = db.Column(db.Date(), nullable= False)
    availability_status = db.Column(db.Text(), nullable= False)
    edition = db.Column(db.String(),nullable = False)
    Summary = db.Column(db.String(), nullable = False)



    def __repr__(self):
        return f"<Book {self.id}>"
    

    def save(self):
        db.session.add(self)
        db.session.commit()



    @classmethod
    def get_by_id(cls,id):
        return cls.query.get_or_404(id)
    


