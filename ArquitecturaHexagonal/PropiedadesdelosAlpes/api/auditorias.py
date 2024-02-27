from flask import Blueprint, request, Response, json
from ..modulos.auditorias.aplicacion.servicios import ServicioAuditoria
from ..modulos.propiedades.aplicacion.dto import PropiedadDTO
from ..seedwork.dominio.excepciones import ExcepcionDominio
from ..modulos.auditorias.aplicacion.mapeadores import MapeadorAuditoriaDTOJson

bp = Blueprint('propiedades', __name__, url_prefix='/propiedades')

@bp.route('/propiedad', methods=('POST',))
def crear_propiedad():
    try:
        propiedad_dict = request.json

        map_propiedad = MapeadorPropiedadDTOJson()
        propiedad_dto = map_propiedad.externo_a_dto(propiedad_dict)

        sp = ServicioPropiedad()
        dto_final = sp.crear_propiedad(propiedad_dto)

        return Response(map_propiedad.dto_a_externo(dto_final), status=200, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps({'error': str(e)}), status=400, mimetype='application/json')

@bp.route('/propiedad/<id>', methods=('GET',))
def obtener_propiedad(id):
    try:
        sp = ServicioPropiedad()
        propiedad_dto = sp.obtener_propiedad_por_id(id)
        
        if propiedad_dto:
            map_propiedad = MapeadorPropiedadDTOJson()
            return Response(map_propiedad.dto_a_externo(propiedad_dto), status=200, mimetype='application/json')
        else:
            return Response(json.dumps({'error': 'Propiedad no encontrada'}), status=404, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps({'error': str(e)}), status=400, mimetype='application/json')
