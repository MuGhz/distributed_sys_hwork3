from peewee import *

sqlite_db = SqliteDatabase('/root/api/database.db')

class BaseModel(Model):
	class Meta:
		database = sqlite_db

class User_count(BaseModel):
	name = CharField(unique=True)
	count = IntegerField(default=0)

def create_tables():
	sqlite_db.connect()
	sqlite_db.create_tables([User_count])

if __name__ == "__main__":
	create_tables()
