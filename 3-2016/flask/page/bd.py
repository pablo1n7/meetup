#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymongo import MongoClient
from models import Noticia,Categoria
from datetime import date

def main():
	client = MongoClient()
	db = client['diario_deportivo']
	# categorias = [Categoria("Futbol").__dict__,Categoria("Tenis").__dict__,Categoria("Hokey").__dict__]
	# db.categorias.insert_many(categorias)

	cat_tenis= db.categorias.find_one({"nombre":"Tenis"})
	cat_futbol = db.categorias.find_one({"nombre":"Futbol"})
	# noticia = Noticia(
	# 	"Arriba la Torre",
	# 	"Juan Martín Del Potro arrancó bien en los primeros games, pero Bautista Agut se despertó y le peleó break a break el primer set, que el tandilense se lo terminó llemando por 7-5. Juan Martín va por el pase a las semifinales de singles. Se juega en el court 2 del Centro Olímpico.",
	# 	"aca va el cuerpo",
	# 	date.today().isoformat(),
	# 	cat_tenis["_id"],
	#	None
	# )
	# db.noticias.insert_one(noticia.__dict__);
	# noticia = Noticia(
	# 	"Sorpresa Decana",
	# 	"Vélez arrancó ganando con gol de Pavone, pero Juventud Unida de Gualeguaychú lo igualó sobre el final y, en los penales, venció al Fortín 4 a 3 y se metió en los octavos de la Copa Argentina.",
	# 	"aca va el cuerpo",
	# 	date.today().isoformat(),
	# 	cat_futbol["_id"],
		# None
	# )
	# db.noticias.insert_one(noticia.__dict__);

	noticia = Noticia(
		"Listo Orion",
		"El arquero se hará este miércoles la revisión médica y luego firmará contrato por dos años con Racing. Con 35 años, Agustín reemplazará a Saja, como ocurrió en San Lorenzo. ",
		"aca va el cuerpo",
		date.today().isoformat(),
		cat_futbol["_id"]
	)

	db.noticias.insert_one(noticia.__dict__)

if __name__ == '__main__':
	main()	