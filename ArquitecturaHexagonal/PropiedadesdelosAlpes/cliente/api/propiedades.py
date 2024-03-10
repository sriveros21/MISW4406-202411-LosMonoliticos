from flask import Blueprint, current_app, jsonify, request, Response, json

from PropiedadesdelosAlpes.modulos.propiedades.aplicacion.queries.obtener_propiedades import ObtenerPropiedad
from ..modulos.propiedades.aplicacion.servicios import ServicioPropiedad
from ..seedwork.dominio.excepciones import ExcepcionDominio
from ..modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedadDTOJson
from ..modulos.propiedades.aplicacion.comandos.crear_propiedad import CrearPropiedad
from PropiedadesdelosAlpes.seedwork.aplicacion.comandos import ejecutar_commando
from PropiedadesdelosAlpes.seedwork.aplicacion.queries import ejecutar_query

bp = Blueprint('propiedades', __name__, url_prefix='/propiedades')

@bp.route('/propiedad', methods=('POST',))
def crear_propiedad():
    try:
        propiedad_dict = request.json
        servicio_propiedad = ServicioPropiedad()
        map_propiedad = MapeadorPropiedadDTOJson()
        propiedad_dto = map_propiedad.externo_a_dto(propiedad_dict)

        dto_final = servicio_propiedad.crear_propiedad(propiedad_dto)

        return Response(json.dumps(map_propiedad.dto_a_externo(dto_final)), status=200, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps({'error': str(e)}), status=400, mimetype='application/json')
    
@bp.route('/propiedad-comando', methods=('POST',))
def crear_propiedad_comando():
    try:
        propiedad_dict = request.json

        map_propiedad = MapeadorPropiedadDTOJson()
        propiedad_dto = map_propiedad.externo_a_dto(propiedad_dict)
        comando = CrearPropiedad(propiedad_dto.id, propiedad_dto.nombre, propiedad_dto.ubicacion, propiedad_dto.dimension, propiedad_dto.tipo, propiedad_dto.estado, propiedad_dto.terreno, propiedad_dto.edificaciones)
        ejecutar_commando(comando)

        return Response(json.dumps({'mensaje': 'Propiedad creada'}), status=200, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps({'error': str(e)}), status=400, mimetype='application/json')

@bp.route('/propiedad/<id>', methods=('GET',))
def obtener_propiedad(id):
    try:
        servicio_propiedad = ServicioPropiedad()
        propiedad_dto = servicio_propiedad.obtener_propiedad_por_id(id)
        if propiedad_dto:
            map_propiedad = MapeadorPropiedadDTOJson()
            return Response(json.dumps(map_propiedad.dto_a_externo(propiedad_dto)), status=200, mimetype='application/json')
        else:
            return Response(json.dumps({'error': 'Propiedad no encontrada'}), status=404, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps({'error': str(e)}), status=400, mimetype='application/json')
    
@bp.route('/propiedad-query/<id>', methods=('GET',))
def obtener_propiedad_query(id):
    try:
        query = ejecutar_query(ObtenerPropiedad(id))
        map_propiedad = MapeadorPropiedadDTOJson()
        return Response(json.dumps(map_propiedad.dto_a_externo(query.resultado)), status=200, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps({'error': str(e)}), status=400, mimetype='application/json')
