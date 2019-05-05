

from abc import ABCMeta, abstractstaticmethod


class Iauto(metaclass=ABCMeta): 
    """interface de auto"""

    @abstractstaticmethod
    def __init__(self,cantidad,precio):
        self._cant =cantidad
        self._prec = precio


class Honda(Iauto): 
    """la clase Honda se implementa de Iauto"""
    def __init__(self,cantidad,precio):
        self._cant =cantidad
        self._prec = precio
        

    def descrip_product(self):
        print("DESCRIPCCION DE PRODUCTO: AUTO")
        print("MARCA: HONDA")
        movil=f"""cantidad: {self._cant} unit\
        precio: {self._prec} soles"""
      
        return movil

    def cotizacion(self):
        print("COTIZACION DE PRODUCTO")
        if self._cant>=4:
            preciot=self._prec*self._cant
            desc=preciot*0.15
            preciof=preciot-desc
        if 0< self._cant<4:
            preciot=self._prec*self._cant
            desc=preciot*0.05
            preciof=preciot-desc
        precTot=f"""precio s/d: {preciot} soles \
        desc: {desc} soles\
        precio c/d: {preciof} soles"""
        return precTot


class Hyundai(Iauto): 
    """la clase Hyundai se implementa de Iauto"""

    def __init__(self,cantidad,precio):
        self._cant =cantidad
        self._prec = precio
        

    def descrip_product(self):
        print("DESCRIPCCION DE PRODUCTO: AUTO")
        print("MARCA: Hyundai")
        movil=f"""cantidad: {self._cant} unit\
        precio: {self._prec} soles"""
      
        return movil

    def cotizacion(self):
        print("COTIZACION DE PRODUCTO")
        if self._cant>=4:
            preciot=self._prec*self._cant
            desc=preciot*0.15
            preciof=preciot-desc
        if 0< self._cant<4:
            preciot=self._prec*self._cant
            desc=preciot*0.05
            preciof=preciot-desc
        precTot=f"""precio s/d: {preciot} soles \
        desc: {desc} soles\
        precio c/d: {preciof} soles"""
        return precTot


class Subaru(Iauto):  
    """la clase Subaru se implementa de Iauto"""

    def __init__(self,cantidad,precio):
        self._cant =cantidad
        self._prec = precio
        

    def descrip_product(self):
        print("DESCRIPCCION DE PRODUCTO: AUTO")
        print("MARCA: Subaru")
        movil=f"""cantidad: {self._cant} unit\
        precio: {self._prec} soles"""
      
        return movil

    def cotizacion(self):
        print("COTIZACION DE PRODUCTO")
        if self._cant>=4:
            preciot=self._prec*self._cant
            desc=preciot*0.15
            preciof=preciot-desc
        if 0< self._cant<4:
            preciot=self._prec*self._cant
            desc=preciot*0.05
            preciof=preciot-desc
        precTot=f"""precio s/d: {preciot} soles \
        desc: {desc} soles\
        precio c/d: {preciof} soles"""
        return precTot


class auto_Factory:  
    """Tha Factory Class"""

    @staticmethod
    def get_marca(tipo):
        """A static method to get a table"""
        cant=int(input("ingresa la cantidad a comprar: \
            "))
        prec=int(input("ingresa el precio por unit: \
            "))
        try:
            if tipo == "honda":
                return Honda(cant,prec)
            if tipo == "hyundai":
                return Hyundai(cant,prec)
            if tipo == "subaru":
                return Subaru(cant,prec)
            raise AssertionError("marca no encontrada")
        except AssertionError as _e:
            print(_e)
        return None


if __name__ == "__main__":
    movil=input("ingresa tu movil")
    tipo_vehiculo = auto_Factory.get_marca(movil)
    print(f"MARCA: {movil}")
    print(tipo_vehiculo.descrip_product())
    print(tipo_vehiculo.cotizacion())