from flask import Blueprint, request, Response, json, current_app, jsonify
from ..modulos.auditorias.aplicacion.servicios import ServicioAuditoria
from ..modulos.auditorias.aplicacion.dto import AuditoriaDTO
from ..seedwork.dominio.excepciones import ExcepcionDominio
from ..modulos.auditorias.aplicacion.mapeadores import MapeadorAuditoriaDTOJson

import PropiedadesdelosAlpes.seedwork.presentacion.api as api
from flask import redirect, render_template,session, url_for
from PropiedadesdelosAlpes.modulos.auditorias.aplicacion.comandos.crear_auditoria import CrearAuditoria
from PropiedadesdelosAlpes.modulos.auditorias.aplicacion.queries.obtener_auditoria import ObtenerAuditoria
from PropiedadesdelosAlpes.seedwork.aplicacion.comandos import ejecutar_commando
from PropiedadesdelosAlpes.seedwork.aplicacion.queries import ejecutar_query


bp = Blueprint('auditorias', __name__, url_prefix='/auditorias')

@bp.route('/auditoria', methods=('POST',))
def crear_auditoria():
    try:
        auditoria_dict = request.json

        map_auditoria = MapeadorAuditoriaDTOJson()
        auditoria_dto = map_auditoria.externo_a_dto(auditoria_dict)

        repositorio = current_app.extensions['repositorio_auditorias']
        mapeador = current_app.extensions['mapeador_auditorias']

        sp = ServicioAuditoria(repositorio=repositorio, mapeador=mapeador)
        dto_final = sp.crear_auditoria(auditoria_dto)
        return Response(json.dumps(map_auditoria.dto_a_externo(dto_final)), status=200, mimetype='application/json')

        #return Response(map_auditoria.dto_a_externo(dto_final), status=200, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps({'error': str(e)}), status=400, mimetype='application/json')

#Auditoria Asincrona
    
@bp.route('/auditoria-comando', methods=('POST',))
def auditoria_asincrona():
    try:
        auditoria_dict = request.json

        map_auditoria = MapeadorAuditoriaDTOJson()
        auditoria_dto = map_auditoria.externo_a_dto(auditoria_dict)

        comando = CrearAuditoria(
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

@bp.route('/auditoria/<id>', methods=('GET',))
def obtener_auditoria(id):
    try:
        repositorio = current_app.extensions['repositorio_auditorias']
        mapeador = current_app.extensions['mapeador_auditorias']       
        sp = ServicioAuditoria(repositorio=repositorio,mapeador=mapeador)
        auditoria_dto = sp.obtener_auditoria_por_id(id)
        
        if auditoria_dto:
            map_auditoria = MapeadorAuditoriaDTOJson()
            return Response(json.dumps(map_auditoria.dto_a_externo(auditoria_dto)), status=200, mimetype='application/json')
            #return Response(map_auditoria.dto_a_externo(auditoria_dto), status=200, mimetype='application/json')
        else:
            return Response(json.dumps({'error': 'Auditoria no encontrada'}), status=404, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps({'error': str(e)}), status=400, mimetype='application/json')


#Usando Query
    
@bp.route('/auditoria-query', methods=('GET',))
@bp.route('/auditoria-query/<id>', methods=('GET',))
def dar_auditoria_usando_query(id=None):
    if id:
        query_resultado = ejecutar_query(ObtenerAuditoria(id))
        map_auditoria = MapeadorAuditoriaDTOJson()
        
        return map_auditoria.dto_a_externo(query_resultado.resultado)
    else:
        return [{'message': 'GET!'}]


#Event Sourcing

@bp.route('/auditoria-event-comando', methods=('POST',))
def auditoria_usando_comando():
    try:
        # NOTE Asignamos el valor 'pulsar' para usar la Unidad de trabajo de Pulsar y 
        # no la defecto de SQLAlchemy
        session['uow_metodo'] = 'pulsar'

        auditoria_dict = request.json

        map_auditoria = MapeadorAuditoriaDTOJson()
        auditoria_dto = map_auditoria.externo_a_dto(auditoria_dict)

        comando = CrearAuditoria(
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

@bp.route('/auditoria-event', methods=('GET',))
@bp.route('/auditoria-event/<id>', methods=('GET',))
def dar_auditoria_usando_query_event(id=None):
    if id:
        query_resultado = ejecutar_query(ObtenerAuditoria(id))
        map_auditoria = MapeadorAuditoriaDTOJson()
        
        return map_auditoria.dto_a_externo(query_resultado.resultado)
    else:
        return [{'message': 'GET!'}]