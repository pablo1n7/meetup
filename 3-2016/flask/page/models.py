
""" CATEGORIA DE UNA NOTICIA: Tenis, Futbol, etc. """
class Categoria(object):

	def __init__(self,nombre,_id=None):
		self.nombre = nombre
		self._id = _id

	def __unicode__(self):
		return '%s' % self.nombre

"""	NOTICIA """
class Noticia(object):

   	def __init__(self, titulo,copete,cuerpo,categoria,fecha=None):
   	 	self.titular = titulo
   	 	self.copete = copete
   	 	self.cuerpo = cuerpo
   	 	self.fecha = fecha
   	 	self.categoria = categoria
	
	def __unicode__(self):
   	 return '%s' % self.titular

""" IMAGEN DE UNA NOTCIA """
class Imagen(object):

	def __init__(self,epigrafe,fuente,_id=None):
		self.epigrafe = epigrafe
		self.fuente = fuente

