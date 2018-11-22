from pyknow import *
import re
class Producto(Fact): # san pham KH da mua
	# Producto(nombre = "pepsi",tipo = "cola",cantidad = 1)
	# nombre: ten, tipo: loai, cantidad: so luong
	pass
class Cupon(Fact): #Phieu giam gia cho lan mua sau
	# Cupon(tipo = "2x1", producto = "pepsi")
	pass

class Promo(Fact): #KM hien tai
	# Promo(tipo = "2x1", **depende_de_la_promo)
	# depende_de_la_promo: phu thuoc vao KM
	pass
	
class Beneficio(Fact): #Loi nhuan thu duoc tu moi san pham
	# Beneficio(nombre = "pepsi", tipo ="cola", ganancias = 0.2) 
	# loi nhuan
	pass
	
class OfertasNxM(KnowledgeEngine):
	@DefFacts()
	def carga_promociones_nxm(self): #hang KM
		# Tao chuong trinh KM hien tai
		yield Promo(tipo = "2x1",producto = "Dodot")
		yield Promo(tipo="2x1", producto="Leche Pascual")
		yield Promo(tipo="3x2", producto="Pilas AAA")

	@Rule(Promo(tipo=MATCH.t & P(lambda t: re.match(r"\d+x\d+",t)),
				producto=MATCH.p),
		  Producto(nombre=MATCH.p))
	def oferta_nxm(self,t,p):
		self.declare(Cupon(tipo=t,producto=p))

class OfertasPACK(KnowledgeEngine): #Don hang goi
	@DefFacts()
	def carga_promociones_pack(self):
		yield Promo(tipo="PACK", producto1="Fregona ACME", producto2="Mopa ACME", descuento="25%")
		yield Promo(tipo="PACK", producto1="Pasta Gallo", producto2="Tomate Frito", descuento="10%")
	# luat nay rang buoc khong duoc mua 2 sp trong 1 don hang
	@Rule(Promo(tipo="PACK", producto1=MATCH.p1, producto2=MATCH.p2, descuento=MATCH.d),
		  OR(
			  AND(
				  NOT(Producto(nombre=MATCH.p1)),
				  Producto(nombre=MATCH.p2)
			  ),
			  AND(
				  Producto(nombre=MATCH.p1),
				  NOT(Producto(nombre=MATCH.p2))
			  )
		  )
		  )
	def pack(self, p1, p2, d):
		"""
        El cliente querrá comprar un producto adicional en su próxima visita.
        """
		self.declare(Cupon(tipo="PACK", producto1=p1, producto2=p2, descuento=d))

class OfertasDescuento(KnowledgeEngine):
	@DefFacts()
	def carga_beneficios(self):
		yield Beneficio(nombre="Mahou", tipo="Cerveza", ganancias=0.5)
		yield Beneficio(nombre="Cerveza Hacendado", tipo="Cerveza", ganancias=0.9)

		yield Beneficio(nombre="Pilas AAA Duracell", tipo="Pilas AAA", ganancias=1.5)
		yield Beneficio(nombre="Pilas AAA Hacendado", tipo="Pilas AAA", ganancias=2)

	@Rule(Producto(nombre=MATCH.p1),
		  Beneficio(nombre=MATCH.p1, tipo=MATCH.t, ganancias=MATCH.g1),
		  Beneficio(nombre=MATCH.p2, tipo=MATCH.t, ganancias=MATCH.g2),
		  TEST(lambda g1, g2: g2 > g1)
		  )
	def descuento_producto_con_mayor_beneficio(self, p2, g1, g2, **_):
		"""
        """
		diferencia_ganancia = g2 - g1
		self.declare(Cupon(tipo="DESCUENTO",
						   producto=p2,
						   cantidad=diferencia_ganancia / 2))


class GeneradorCupones(OfertasNxM, OfertasPACK, OfertasDescuento):
	def generar_cupones(self, *nombre_productos):
		# Reiniciamos el motor
		self.reset()

		# Declaramos los productos que ha comprado el cliente
		for nombre in nombre_productos:
			self.declare(Producto(nombre=nombre))

		# Ejecutamos el motor
		self.run()

		# Extraemos las promociones generadas
		for fact in self.facts.values():
			if isinstance(fact, Cupon):
				yield fact

watch('RULES','FACTS')
# nxm = OfertasNxM()
# nxm.reset()
# nxm.declare(Producto(nombre="Dodot"))
# nxm.declare(Producto(nombre="Agua Mineral"))
# nxm.declare(Producto(nombre="Pilas AAA"))
# nxm.run()
# nxm.facts
# pack = OfertasPACK()
# pack.reset()
# pack.declare(Producto(nombre = "Tomate Frito"))
# pack.declare(Producto(nombre="Fregona ACME"))
# pack.declare(Producto(nombre="Mopa ACME"))
# pack.run()
# pack.facts
# descuento = OfertasDescuento()
# # descuento.reset()
# # # descuento.declare(Producto(nombre="Mahou"))
# # descuento.declare(Producto(nombre="Pilas AAA Hacendado"))
# # descuento.run()
ke = GeneradorCupones()
[cupon for cupon in ke.generar_cupones("Pilas AAA", "Mahou", "Tomate Frito")]