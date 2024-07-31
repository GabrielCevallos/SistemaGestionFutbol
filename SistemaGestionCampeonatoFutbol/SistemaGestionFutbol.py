from enum import Enum, auto
from typing import List

class Tarjeta(Enum):
    AMARILLA = auto()
    ROJA = auto()

class Estado(Enum):
    TITULAR = auto()
    SUPLENTE = auto()
    EXPULSADO = auto()

class Genero(Enum):
    MASCULINO = auto()
    FEMENINO = auto()

class PosicionEquipo(Enum):
    ARQUERO = auto()
    DEFENSOR = auto()
    MEDIOCAMPISTA = auto()
    DELANTERO = auto()

class SistemaCampeonato(Enum):
    LIGA = auto()
    MUERTE_SUBITA = auto()
    FASE_GRUPOS = auto()

class Estadistica:
    def __init__(self):
        self.nro_penalizaciones = 0
        self.nro_total_goles = 0
        self.nro_total_remates_arco = 0
        self.nro_total_tiro_esquina = 0
        self.presion_pases = 0
        self.posesion_balon = 0
        self.nro_total_pases = 0

class EstadisticaEquipo(Estadistica):
    def __init__(self):
        super().__init__()
        self.nro_puntos_partido = 0

class EstadisticaIndividual(Estadistica):
    def __init__(self):
        super().__init__()
        self.nro_total_tarjetas = 0

class TablaPosicion:
    def __init__(self):
        self.puntos_equipo = 0
        self.lider_tabla = ""
        self.tabla_posicion_list = []

    def registrar_puntos_equipo(self, puntos_tabla):
        self.puntos_equipo = puntos_tabla

    def sumar_puntos_equipo(self, puntos_tabla):
        self.puntos_equipo += puntos_tabla

    def mostrar_tabla_posiciones(self):
        print("Tabla de Posiciones:")
        for tp in self.tabla_posicion_list:
            print(f"{tp.lider_tabla}: {tp.puntos_equipo} puntos")

class Campeonato:
    def __init__(self, fecha, numero_fechas, grupos, nro_grupos):
        self.fecha = fecha
        self.numero_fechas = numero_fechas
        self.grupos = grupos
        self.nro_grupos = nro_grupos
        self.deporte_list = []
        self.inscripcion_list = []

    def iniciar_campeonato(self):
        print("Campeonato iniciado")
        return True

    def finalizar_campeonato(self):
        print("Campeonato finalizado")
        return True

    def sortear_equipos(self):
        print("Equipos sorteados")

class Deporte:
    def __init__(self, nombre, nro_participantes_equipo, nro_partidos, reglamento):
        self.nombre = nombre
        self.nro_participantes_equipo = nro_participantes_equipo
        self.nro_partidos = nro_partidos
        self.reglamento = reglamento
        self.grupo_list = []

class Grupo:
    def __init__(self, nombre, nro_equipos):
        self.nombre = nombre
        self.nro_equipos = nro_equipos
        self.equipo_list = []

    def asignar_nro_partidos_grupo(self):
        print(f"Número de partidos asignados para el grupo {self.nombre}")

class Inscripcion:
    def __init__(self, costo):
        self.costo = costo

    def iniciar_inscripciones(self):
        print("Inscripciones iniciadas")
        return True

    def finalizar_inscripciones(self):
        print("Inscripciones finalizadas")
        return True

    def realizar_pago_inscripcion(self, equipo):
        print(f"Pago de inscripción realizado para el equipo: {equipo.nombre}")
        return True

class Arbitro:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tarjeta_list = []

    def penalizar_jugador(self, jugador, tarjeta):
        self.tarjeta_list.append(tarjeta)
        print(f"Jugador {jugador.numero} penalizado con tarjeta {tarjeta.name}")
        return True

class Equipo:
    def __init__(self, nombre, nro_jugadores):
        self.nombre = nombre
        self.nro_jugadores = nro_jugadores
        self.puntos_tabla = 0
        self.nro_partidos_jugados = 0
        self.nro_partidos_ganados = 0
        self.nro_partidos_empatados = 0
        self.nro_partidos_perdidos = 0
        self.nro_total_goles = 0
        self.nro_goles_contra = 0
        self.nro_penalizaciones = 0
        self.jugador_list = []
        self.partido_list = []

class Jugador:
    def __init__(self, numero):
        self.numero = numero
        self.nro_goles = 0
        self.nro_tarjetas_recibidas = 0

    def anotar_gol(self, nro_goles):
        self.nro_goles += nro_goles
        print(f"Jugador {self.numero} ha anotado {nro_goles} gol(es).")
        return True

class Partido:
    def __init__(self, duracion_minutos, arbitro, numero_arbitros, marcador):
        self.duracion_minutos = duracion_minutos
        self.arbitro = arbitro
        self.numero_arbitros = numero_arbitros
        self.marcador = marcador

    def iniciar_partido(self):
        print("Partido iniciado")
        return True

    def pausar_partido(self):
        print("Partido pausado")
        return True

    def reanudar_partido(self):
        print("Partido reanudado")
        return True

    def finalizar_partido(self):
        print("Partido finalizado")
        return True

    def determinar_resultado(self):
        print(f"El resultado del partido es: {self.marcador}")

if __name__ == "__main__":
    inscripcion = Inscripcion(100)
    inscripcion.iniciar_inscripciones()

    equipo1 = Equipo("Equipo A", 11)
    equipo2 = Equipo("Equipo B", 11)

    inscripcion.realizar_pago_inscripcion(equipo1)
    inscripcion.realizar_pago_inscripcion(equipo2)
    inscripcion.finalizar_inscripciones()

    campeonato = Campeonato(2023, 10, "Grupo 1", 1)
    campeonato.iniciar_campeonato()
    campeonato.sortear_equipos()

    grupo1 = Grupo("Grupo 1", 2)
    grupo1.equipo_list.append(equipo1)
    grupo1.equipo_list.append(equipo2)
    grupo1.asignar_nro_partidos_grupo()

    arbitro = Arbitro("Arbitro 1")

    jugador1 = Jugador(1)
    jugador2 = Jugador(2)
    jugador3 = Jugador(3)
    jugador4 = Jugador(4)

    equipo1.jugador_list.append(jugador1)
    equipo1.jugador_list.append(jugador2)
    equipo2.jugador_list.append(jugador3)
    equipo2.jugador_list.append(jugador4)

    partido = Partido(90, "Arbitro 1", 1, "0 - 0")
    partido.iniciar_partido()

    jugador1.anotar_gol(1)
    jugador3.anotar_gol(1)
    jugador2.anotar_gol(1)
    jugador4.anotar_gol(1)

    arbitro.penalizar_jugador(jugador1, Tarjeta.AMARILLA)
    arbitro.penalizar_jugador(jugador3, Tarjeta.ROJA)

    partido.marcador = "2 - 2"
    partido.finalizar_partido()
    partido.determinar_resultado()

    tabla_posicion = TablaPosicion()
    tabla_posicion.registrar_puntos_equipo(1)
    tabla_posicion.sumar_puntos_equipo(1)

    tabla_posicion.tabla_posicion_list.append(tabla_posicion)
    tabla_posicion.lider_tabla = equipo1.nombre
    tabla_posicion.mostrar_tabla_posiciones()

    tabla_posicion.lider_tabla = equipo2.nombre
    tabla_posicion.mostrar_tabla_posiciones()