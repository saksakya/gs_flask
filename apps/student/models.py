from datetime import datetime

from apps.app import db

class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String, unique=True, index=True)
    nickname = db.Column(db.String, index=True)
    p_flag = db.Column(db.Boolean, default=False)
    group01 = db.Column(db.String)
    group02 = db.Column(db.String)
    group03 = db.Column(db.String)
    group04 = db.Column(db.String)
    group05 = db.Column(db.String)
    group06 = db.Column(db.String)
    group07 = db.Column(db.String)
    group08 = db.Column(db.String)
    group09 = db.Column(db.String)
    group10 = db.Column(db.String)
    group11 = db.Column(db.String)
    group12 = db.Column(db.String)
    group13 = db.Column(db.String)
    group14 = db.Column(db.String)
    group15 = db.Column(db.String)
    group16 = db.Column(db.String)
    group17 = db.Column(db.String)
    group18 = db.Column(db.String)
    group19 = db.Column(db.String)
    group20 = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    
    def is_duplicate_number(self):
        return Student.query.filter_by(number=self.number).first() is not None