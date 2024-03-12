import PropiedadesdelosAlpes.cliente.seedwork.presentacion.api as api
from flask import request, Response, json, session

from ..modulos.cliente.aplicacion.mapeadores import MapeadorClienteDTOJson
from ..seedwork.dominio.excepciones import ExcepcionDominio

bp = api.crear_blueprint('cliente', '/cliente')


@bp.route('/cliente', methods=('POST',))
def cliente_usando_comando():
    try:
        session['uow_metodo'] = 'pulsar'

        cliente_dict = request.json

        map_cliente = MapeadorClienteDTOJson()
        cliente_dto = map_cliente.externo_a_dto(cliente_dict)

        comando = CrearCliente(
            cliente_dto.id_cliente,
            cliente_dto.nombre,
            cliente_dto.apellido,
            cliente_dto.email
        )

        ejecutar_commando(comando)

        return Response('{}', status=200, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')


@bp.route('/cliente', methods=('GET',))
@bp.route('/cliente/<id_cliente>', methods=('GET',))
def dar_cliente_usando_query_event(id_cliente=None):
    if id:
        query_resultado = ejecutar_query(ObtenerCliente(id))
        map_cliente = MapeadorClienteDTOJson()

        return map_cliente.dto_a_externo(query_resultado.resultado)
    else:
        return [{'message': 'GET!'}]
