from flask import Blueprint, current_app, jsonify, request, Response, json

from PropiedadesdelosAlpes.propiedades.modulos.aplicacion.dto import PropiedadDTO
from PropiedadesdelosAlpes.propiedades.modulos.aplicacion.queries.obtener_propiedades import ObtenerPropiedad

from ...propiedades.modulos.aplicacion.mapeadores import MapeadorPropiedadDTOJson
from ...propiedades.modulos.aplicacion.comandos.crear_propiedad import CrearPropiedad
from PropiedadesdelosAlpes.seedwork.aplicacion.comandos import ejecutar_commando
from PropiedadesdelosAlpes.seedwork.aplicacion.queries import ejecutar_query

bp = Blueprint('propiedades', __name__, url_prefix='/propiedades')

@bp.route('/propiedad', methods=('POST',))
def propiedad_usando_comando():
    try:
        session['uow_metodo'] = 'pulsar'

        propiedad_dict = request.json

        map_propiedad = MapeadorPropiedadDTOJson()
        propiedad_dto = map_propiedad.externo_a_dto(propiedad_dict)
        comando = CrearPropiedad(propiedad_dto.id, propiedad_dto.nombre, propiedad_dto.ubicacion, propiedad_dto.dimension, propiedad_dto.tipo, propiedad_dto.estado, propiedad_dto.terreno, propiedad_dto.edificaciones)
        ejecutar_commando(comando)

        return Response(json.dumps(map_propiedad.dto_a_externo(dto_final)), status=200, mimetype='application/json')
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
