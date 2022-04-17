# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo
# model the class after the friend table from our database
class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo = {}

    @classmethod
    def create( cls, data ):
        query = "INSERT INTO ninjas ( first_name , last_name , age , dojo_id , created_at , updated_at ) VALUES (%(fname)s, %(lname)s, %(age)s, %(dojo_id)s, NOW(), NOW());"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)

    @classmethod
    def get_ninjas_with_dojo( cls, data ):
        query = "SELECT * FROM ninjas LEFT JOIN dojos ON dojo_id = dojos.id WHERE dojos.id = %(id)s"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

        ninjas = []

        for row in results:
            ninja = cls(row)
            dojo_data = {
            "id" : row['dojos.id'],
            "name" : row['name'],
            "created_at" : row['dojos.created_at'],
            "updated_at" : row['dojos.updated_at'],
            }

            ninja.dojo = dojo.Dojo(dojo_data)
            ninjas.append(ninja)

        return ninjas