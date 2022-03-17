

from pymongo import MongoClient

from ResponseModel import ResponseModel


class DBHandler(object):
    def __init__(self):
        self.db = self.conectar()
        self.collection = self.db.get_collection('estudiantes')


   
    def conectar(self):
        connection_url = 'mongodb+srv://Ivan:1234@cluster0.lwsix.mongodb.net/tienda?retryWrites=true&w=majority'
        client = MongoClient(connection_url)
        db = client.get_database('tienda')
        SampleTable = db.SampleTable
        return db

    

###################################################
#################  PRODUCTOS  #####################
###################################################

    def eliminarProducto(self,_idP):
        response = ResponseModel()
        try:
            self.collection = self.db.get_collection('productos')
            self.collection.delete_one({'_id':_idP})
            response.resultOK = True
            response.data = 'Eliminado correctamente'
        except Exception as e:
            print(e)

        return response


    def obtenerProducto(self,_idP):
        response = ResponseModel()
        try:
            self.collection = self.db.get_collection('productos')
            producto = self.collection.find_one({'_id':_idP})
            if producto is None:
                response.resultOK = False
                response.data = "No se ha encontrado ningún producto con ese ID"
            else:
                response.resultOK = True
                response.data = str(producto)
        except Exception as e:
            print(e)

        return response


    def actualizarProducto(self, producto):
        response = ResponseModel()
        #print(producto['Nombre'])

        try:
            self.collection = self.db.get_collection('productos')
            self.collection.update_one({'_id':producto['_id']},{'$set':producto})
            response.resultOK = True
            response.data = 'Producto actualizado con éxito'
        except Exception as e:
            print(e)

        return response


    def obtenerProductos(self):
        response = ResponseModel()
        try:
            self.collection = self.db.get_collection('productos')
            listaProductos = []
            coleccion = self.collection.find({})
            for productos in coleccion:
                listaProductos.append(productos)

            response.resultOK = True
            response.data = str(listaProductos)

        except Exception as e:
            print(e)

        return response



    def insertarProducto(self, producto):
        response = ResponseModel()
        #producto = self.collection.find_one({'_id':producto['_idP']})
        try:
            self.collection = self.db.get_collection('productos')
            result = self.collection.insert_one(producto)
            print(result)

            response.resultOK = True
            response.data = 'Producto insertado con éxito'
        except Exception as e:
            print(e)


        return response