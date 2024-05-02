from abc import ABC, abstractmethod
from datetime import date

class CuentaBancaria(ABC):  
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo = 0):
        self._nombre_titular = nombre_titular
        self._dni_titular = dni_titular
        self._fecha_nacimiento = fecha_nacimiento
        self._saldo = saldo
    

    @abstractmethod
    def depositar_dinero(self, monto_depositado):
       pass
        

    @abstractmethod
    def extraer_dinero(self, monto):
        pass

    def traer_nombre_titular(self):
        return self._nombre_titular
    
    def traer_dni_titular(self):
        return self._dni_titular
    
    def traer_fecha_nacimiento(self):
        return self._fecha_nacimiento

    def _obtener_edad(self):
        fecha_actual = date.today()
        edad = fecha_actual - traer_fecha_nacimiento()
        return edad.days // 365
    
    def traer_saldo(self):
        return self._saldo
    
    def modificar_nombre_titular(self, nuevo_nombre):
        self._nombre_titular = nuevo_nombre
    
    def modificar_dni_titular(self, nuevo_dni):
        self._dni_titular = nuevo_dni
    
    def modificar_fecha_nacimiento(self, nueva_fecha_nacimiento):
        self._fecha_nacimiento= nueva_fecha_nacimiento
    
    


class CuentaAhorro(CuentaBancaria):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo = 0, tasa_interes = 0.001 ):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)
        self._tasa_interes = tasa_interes
    

    
    
    def depositar_dinero(self, monto_depositado):
        if monto_depositado > 0:
            self._saldo += monto_depositado
            print(f'Ud. ha depositado {monto_depositado} en la cuenta de {self.traer_nombre_titular()}, su saldo actual es: ${self.traer_saldo()}')
        else:
            print("No se puede depositar un monton menor o igual a 0")
        

    def extraer_dinero(self, monto):
        if self._saldo >= monto:
            self._saldo -= monto
            print(f'Ud. ha retirado $ {monto} de la cuenta de {self.traer_nombre_titular()}, su saldo actual es: {self.traer_saldo()}')
        else:
            print('Ud. no posee saldo suficiente para realizar la extraccion')


    def calcular_interes(self):
        interes_resultante =  super().traer_saldo() * self._tasa_interes
        print(f'El interes resultante de su caja de ahorro es: $ {interes_resultante} ')
        return interes_resultante


cajaDeAhorro1 = CuentaAhorro("ramiro quinoneros", 23209377, date(1973,6,8), 500)
print(f'Caja de Ahorro a nombre de {cajaDeAhorro1.traer_nombre_titular()}, con dni: {cajaDeAhorro1.traer_dni_titular()}, fecha de nacimiento: {cajaDeAhorro1.traer_fecha_nacimiento()}, saldo actual: $ {cajaDeAhorro1.traer_saldo()} ')
cajaDeAhorro1.depositar_dinero(150000)
cajaDeAhorro1.extraer_dinero(150)
cajaDeAhorro1.calcular_interes()
cajaDeAhorro1.depositar_dinero(0)
cajaDeAhorro1.extraer_dinero(15000000)