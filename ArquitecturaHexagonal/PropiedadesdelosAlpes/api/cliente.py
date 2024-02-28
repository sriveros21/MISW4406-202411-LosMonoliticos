from flask import Blueprint, request, Response, json

from ..modulos.cliente.aplicacion.mapeadores import MapeadorClienteDTOJson
from ..modulos.cliente.aplicacion.servicios import ServicioCliente
from ..seedwork.dominio.excepciones import ExcepcionDominio

bp = Blueprint('cliente', __name__, url_prefix='/cliente')


@bp.route('/cliente', methods=('POST',))
def crear_cliente():
    try:
        cliente_dict = request.json

        map_cliente = MapeadorClienteDTOJson()
        cliente_dto = map_cliente.externo_a_dto(cliente_dict)

        sp = ServicioCliente()
        dto_final = sp.crear_cliente(cliente_dto)

        return Response(map_cliente.dto_a_externo(dto_final), status=200, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps({'error': str(e)}), status=400, mimetype='application/json')


@bp.route('/cliente/<id>', methods=('GET',))
def obtener_cliente(id):
    try:
        sp = ServicioCliente()
        cliente_dto = sp.obtener_cliente_por_id(id)

        if cliente_dto:
            map_cliente = MapeadorClienteDTOJson()
            return Response(map_cliente.dto_a_externo(cliente_dto), status=200, mimetype='application/json')
        else:
            return Response(json.dumps({'error': 'Cliente no encontrado'}), status=404, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps({'error': str(e)}), status=400, mimetype='application/json')
