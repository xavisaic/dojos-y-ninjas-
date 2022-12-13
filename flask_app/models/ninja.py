from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name= data['first_name']
        self.last_name= data['last_name']
        self.age= data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO ninjas (first_name, last_name, age, created_at,updated_at, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, NOW(),NOW(), %(dojo_id)s)"
        return connectToMySQL('dojosyninjas_schema').query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        ninjas_from_db =  connectToMySQL('dojosyninjas_schema').query_db(query)
        ninjas =[]
        for b in ninjas_from_db:
            ninjas.append(cls(b))
        return ninjas

    @classmethod
    def get_from(cls, data):
        query = "SELECT * FROM ninjas JOIN dojos ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s"
        ninjas_from_db =  connectToMySQL('dojosyninjas_schema').query_db(query, data)
        return ninjas_from_db


    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM ninjas WHERE ninjas.id = %(id)s;"
        ninja_from_db = connectToMySQL('dojosyninjas_schema').query_db(query,data)

        return cls(ninja_from_db[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE ninjas SET name=%(first_name)s, %(last_name)s, %(age)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('dojosyninjas_schema').query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL('dojosyninjas_schema').query_db(query,data)
