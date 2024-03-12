from PropiedadesdelosAlpes.auditoria.seedwork.aplicacion.sagas import CoordinadorOrquestacion, Transaccion, Inicio, Fin
from PropiedadesdelosAlpes.auditoria.seedwork.aplicacion.comandos import Comando
from PropiedadesdelosAlpes.auditoria.seedwork.dominio.eventos import EventoDominio

from PropiedadesdelosAlpes.auditoria.modulos.aplicacion.comandos.crear_auditoria import CrearAuditoria
from PropiedadesdelosAlpes.auditoria.modulos.dominio.eventos.auditorias import AuditoriaCreada


class CoordinadorAuditorias(CoordinadorOrquestacion):

    def inicializar_pasos(self):
        self.pasos = [
            Inicio(index=0),
            Transaccion(index=1, comando=CrearAuditoria, evento=AuditoriaCreada, error=None, compensacion=None),
            Fin(index=2)
        ]

    def iniciar(self):
        self.persistir_en_saga_log(self.pasos[0])
    
    def terminar():
        self.persistir_en_saga_log(self.pasos[-1])

    def persistir_en_saga_log(self, mensaje):
        # TODO Persistir estado en DB
        # Probablemente usted podría usar un repositorio para ello
        saga_log_entry = SagaLog(
            saga_id=self.saga_id,
            paso_index=paso.index,
            estado=str(paso)
        )
        self.session.add(saga_log_entry)
        self.session.commit()

    def construir_comando(self, evento: EventoDominio, tipo_comando: type):
        # TODO Transforma un evento en la entrada de un comando
        # Por ejemplo si el evento que llega es ReservaCreada y el tipo_comando es PagarReserva
        # Debemos usar los atributos de ReservaCreada para crear el comando PagarReserva
        def construir_comando(self, evento: EventoDominio, tipo_comando: type):
            if isinstance(evento, AuditoriaCreada) and tipo_comando is CrearAuditoria:
                return CrearAuditoria(
                    id_auditoria=evento.id_auditoria,
                    codigo=evento.codigo,
                    fecha_creacion=evento.fecha_creacion,
                    auditor=evento.auditor,
                    fase=evento.fase,
                    hallazgos=evento.hallazgos,
                    objetivo=evento.objetivo
                )
            else:
                raise ValueError("Unsupported command type or event type")


# TODO Agregue un Listener/Handler para que se puedan redireccionar eventos de dominio
def oir_mensaje(mensaje):
    if isinstance(mensaje, EventoDominio):
        coordinador = CoordinadorAuditorias()
        coordinador.procesar_evento(mensaje)
    else:
        raise NotImplementedError("El mensaje no es evento de Dominio")