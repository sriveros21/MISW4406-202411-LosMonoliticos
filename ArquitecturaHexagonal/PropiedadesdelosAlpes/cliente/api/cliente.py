from PropiedadesdelosAlpes.modulos.cliente.aplicacion.comandos.crear_cliente import CrearCliente
from PropiedadesdelosAlpes.modulos.cliente.aplicacion.consultas.consultar_cliente import ObtenerCliente
from PropiedadesdelosAlpes.modulos.cliente.aplicacion.mapeadores import MapeadorClienteDTOJson
from PropiedadesdelosAlpes.modulos.cliente.aplicacion.servicios import ServicioCliente
from PropiedadesdelosAlpes.seedwork.aplicacion.comandos import ejecutar_commando
from PropiedadesdelosAlpes.seedwork.aplicacion.queries import ejecutar_query
from PropiedadesdelosAlpes.seedwork.dominio.excepciones import ExcepcionDominio
from flask import Blueprint, request, Response, json, current_app

bp = Blueprint('cliente', __name__, url_prefix='/cliente')


@bp.route('/cliente', methods=('POST',))
def crear_cliente():
    try:
        cliente_dict = request.json

        map_cliente = MapeadorClienteDTOJson()
        cliente_dto = map_cliente.externo_a_dto(cliente_dict)

        repositorio = current_app.extensions['repositorio_cliente']
        mapeador = current_app.extensions['mapeador_cliente']

        sc = ServicioCliente(repositorio=repositorio, mapeador=mapeador)
        dto_final = sc.crear_cliente(cliente_dto)
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

        if cliente_dto:
            map_cliente = MapeadorClienteDTOJson()
            return Response(json.dumps(map_cliente.dto_a_externo(cliente_dto)), status=200, mimetype='application/json')
        else:
            return Response(json.dumps({'error': 'Cliente no encontrado'}), status=404, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps({'error': str(e)}), status=400, mimetype='application/json')


@bp.route('/cliente-comando', methods=['POST', ])
def cliente_asincrono():
    try:
        cliente_dict = request.get_json()

        map_cliente = MapeadorClienteDTOJson()
        cliente_dto = map_cliente.externo_a_dto(cliente_dict)

        comando = CrearCliente(
            cliente_dto.id_cliente,
            cliente_dto.nombre,
            cliente_dto.apellido,
            cliente_dto.email)

        ejecutar_commando(comando)
        return Response(json.dumps({'mensaje': 'Cliente creado'}), status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')


@bp.route('/cliente-query', methods=('GET',))
@bp.route('/cliente-query/<id>', methods=('GET',))
def dar_cliente_usando_query(id=None):
    if id:
        query_resultado = ejecutar_query(ObtenerCliente(id))
        map_cliente = MapeadorClienteDTOJson()

        return map_cliente.dto_a_externo(query_resultado.resultado)
    else:
        return [{'message': 'GET!'}]
