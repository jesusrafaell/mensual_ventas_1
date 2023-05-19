class Resumen:
    def __init__(self, afiliado, terminal, comercio, ubicacion, doeContador, doeMonto, dbncContador, dbncMonto, dpContador, dpMonto, voeContador, voeMonto, vbncContador, vbncMonto, moeContador, moeMonto, mbncContador, mbncMonto):
        self.afiliado = afiliado
        self.terminal = terminal
        self.comercio = comercio
        self.ubicacion = ubicacion
        self.doeContador = doeContador
        self.doeMonto = doeMonto
        self.dbncContador = dbncContador
        self.dbncMonto = dbncMonto
        self.dpContador = dpContador
        self.dpMonto = dpMonto
        self.voeContador = voeContador
        self.voeMonto = voeMonto
        self.vbncContador = vbncContador
        self.vbncMonto = vbncMonto
        self.moeContador = moeContador
        self.moeMonto = moeMonto
        self.mbncContador = mbncContador
        self.mbncMonto = mbncMonto
        
    def __str__(self):
        return (f"Afiliado: {self.afiliado}\n"
                f"Terminal: {self.terminal}\n"
                f"Comercio: {self.comercio}\n"
                f"Ubicación: {self.ubicacion}\n"
                f"DOE contador: {self.doeContador}, monto: {self.doeMonto}\n"
                f"DBNC contador: {self.dbncContador}, monto: {self.dbncMonto}\n"
                f"DP contador: {self.dpContador}, monto: {self.dpMonto}\n"
                f"VOE contador: {self.voeContador}, monto: {self.voeMonto}\n"
                f"VBNC contador: {self.vbncContador}, monto: {self.vbncMonto}\n"
                f"MOE contador: {self.moeContador}, monto: {self.moeMonto}\n"
                f"MBNC contador: {self.mbncContador}, monto: {self.mbncMonto}")