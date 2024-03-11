from flask import Blueprint, request, Response, json, current_app, jsonify
from ..modulos.aplicacion.dto import AuditoriaDTO
from ..seedwork.dominio.excepciones import ExcepcionDominio
from ..modulos.aplicacion.mapeadores import MapeadorAuditoriaDTOJson

import PropiedadesdelosAlpes.auditoria.seedwork.presentacion.api as api
from flask import redirect, render_template,session, url_for
from PropiedadesdelosAlpes.auditoria.modulos.aplicacion.comandos.crear_auditoria import CrearAuditoria
from PropiedadesdelosAlpes.auditoria.modulos.aplicacion.queries.obtener_auditoria import ObtenerAuditoria
from PropiedadesdelosAlpes.auditoria.seedwork.aplicacion.comandos import ejecutar_commando
from PropiedadesdelosAlpes.auditoria.seedwork.aplicacion.queries import ejecutar_query

bp = api.crear_blueprint('auditorias', '/auditorias')
#bp = Blueprint('auditorias', __name__, url_prefix='/auditorias')

#Event Sourcing
@bp.route('/auditoria', methods=('POST',))
def auditoria_usando_comando():
    try:
        # NOTE Asignamos el valor 'pulsar' para usar la Unidad de trabajo de Pulsar y 
        # no la defecto de SQLAlchemy
        session['uow_metodo'] = 'pulsar'

        auditoria_dict = request.json

        map_auditoria = MapeadorAuditoriaDTOJson()
        auditoria_dto = map_auditoria.externo_a_dto(auditoria_dict)

        comando = CrearAuditoria(
            auditoria_dto.id,
            auditoria_dto.id_auditoria,
            auditoria_dto.codigo_auditoria, 
            auditoria_dto.fecha_auditoria, 
            auditoria_dto.nombre_auditor, 
            auditoria_dto.fase_auditoria,
            auditoria_dto.hallazgos_auditoria, 
            auditoria_dto.objetivo_auditoria)

        
        # TODO Reemplaze es todo código sincrono y use el broker de eventos para propagar este comando de forma asíncrona
        # Revise la clase Despachador de la capa de infraestructura
        ejecutar_commando(comando)
        
        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/auditoria', methods=('GET',))
@bp.route('/auditoria/<id>', methods=('GET',))
def dar_auditoria_usando_query_event(id=None):
    if id:
        query_resultado = ejecutar_query(ObtenerAuditoria(id))
        map_auditoria = MapeadorAuditoriaDTOJson()
        
        return map_auditoria.dto_a_externo(query_resultado.resultado)
    else:
        return [{'message': 'GET!'}]