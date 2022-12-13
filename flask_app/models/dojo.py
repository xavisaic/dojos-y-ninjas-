from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name= data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos (name,created_at,updated_at) VALUES (%(name)s,NOW(),NOW())"
        return connectToMySQL('dojosyninjas_schema').query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        dojos_from_db =  connectToMySQL('dojosyninjas_schema').query_db(query)
        dojos =[]
        for b in dojos_from_db:
            dojos.append(cls(b))
        return dojos

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM dojos WHERE dojos.id = %(id)s;"
        dojo_from_db = connectToMySQL('dojosyninjas_schema').query_db(query,data)

        return cls(dojo_from_db[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE dojos SET name=%(name)s,updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('dojosyninjas_schema').query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL('dojosyninjas_schema').query_db(query,data)
