from django.db import models


#Ejemplo de creacion de tablas en db
#class TABLE_NAME(Models.Model)
class login(models.Model):
	#nombre_columna = models.(tipo de columna, consultar api https://docs.djangoproject.com/en/1.8/topics/db/models/#field-types ).
	user_name = models.CharField(max_length=10)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=100)



