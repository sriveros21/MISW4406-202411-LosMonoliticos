from flask import Blueprint, request, Response, json
from ..modulos.auditorias.aplicacion.servicios import ServicioAuditoria
from ..modulos.propiedades.aplicacion.dto import PropiedadDTO
from ..seedwork.dominio.excepciones import ExcepcionDominio
from ..modulos.auditorias.aplicacion.mapeadores import MapeadorAuditoriaDTOJson

bp = Blueprint('auditorias', __name__, url_prefix='/auditorias')

@bp.route('/auditoria', methods=('POST',))
def crear_auditoria():
    try:
        auditoria_dict = request.json

        map_auditoria = MapeadorAuditoriaDTOJson()
        auditoria_dto = map_auditoria.externo_a_dto(auditoria_dict)

        sp = ServicioAuditoria()
        dto_final = sp.crear_auditoria(auditoria_dto)

        return Response(map_auditoria.dto_a_externo(dto_final), status=200, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps({'error': str(e)}), status=400, mimetype='application/json')

@bp.route('/auditoria/<id>', methods=('GET',))
def obtener_auditoria(id):
    try:
        sp = ServicioAuditoria()
        auditoria_dto = sp.obtener_auditoria_por_id(id)
        
        if auditoria_dto:
            map_auditoria = MapeadorAuditoriaDTOJson()
            return Response(map_auditoria.dto_a_externo(auditoria_dto), status=200, mimetype='application/json')
        else:
            return Response(json.dumps({'error': 'Propiedad no encontrada'}), status=404, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps({'error': str(e)}), status=400, mimetype='application/json')
