from flask import Blueprint, request, Response, json, current_app

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

        print(cliente_dto)  # Print the value of cliente_dto
        repositorio = current_app.extensions['repositorio_cliente']
        mapeador = current_app.extensions['mapeador_cliente']
        sc = ServicioCliente(repositorio=repositorio, mapeador=mapeador)
        dto_final = sc.crear_cliente(cliente_dto)
        print(dto_final)  # Print the value of dto_final

        return Response(json.dumps(map_cliente.dto_a_externo(dto_final)), status=200, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps({'error': str(e)}), status=400, mimetype='application/json')


@bp.route('/cliente/<id_cliente>', methods=('GET',))
def obtener_cliente(id_cliente):
    try:
        repositorio = current_app.extensions['repositorio_cliente']
        mapeador = current_app.extensions['mapeador_cliente']
        sc = ServicioCliente(repositorio=repositorio, mapeador=mapeador)
        cliente_dto = sc.obtener_cliente_por_id(id_cliente)
        print("CLIENTE DTO", cliente_dto)  # Print the value of cliente_dto

        if cliente_dto:
            map_cliente = MapeadorClienteDTOJson()
            return Response(json.dumps(map_cliente.dto_a_externo(cliente_dto)), status=200, mimetype='application/json')
        else:
            return Response(json.dumps({'error': 'Cliente no encontrado'}), status=404, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps({'error': str(e)}), status=400, mimetype='application/json')
