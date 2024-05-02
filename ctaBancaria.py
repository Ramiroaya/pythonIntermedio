class CuentaBancaria:
    def __init__(self, nombre_titula, dni_titular, fecha_nacimiento, saldo = 0 ):
        self._nombre_titular = nombre_titular
        self._dni_titular = dni_titular
        self._fecha_nacimiento = fecha_nacimiento
        self._saldo = saldo
    

    def traer_nombre_titular(self):
        return self._nombre_titular
    
    def traer_dni_titular(self):
        return self._dni_titular
    
    def traer_fecha_nacimiento(self):
        return self._fecha_nacimiento
    
    def traer_saldo(self):
        return self._saldo
    


class CuentaCorriente(CuentaBancaria):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo = 0, limite_extraccion = 500):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)
        self._limite_extraccion = limite_extraccion