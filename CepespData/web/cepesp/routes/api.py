from botocore.exceptions import ClientError
from flask import request, jsonify
from werkzeug.exceptions import BadRequest, NotFound

from web.cepesp.athena.client import AthenaQueryFailed
from web.cepesp.athena.options import AthenaQueryOptions, AthenaResultOptions
from web.cepesp.athena.query import AthenaQuery, QueryNotFoundException
from web.cepesp.config import API_PYTHON_VERSION, API_R_VERSION
from web.cepesp.routes.lang import lang
from web.cepesp.utils.analytics import track_event
from web.cepesp.utils.output import ResponseConverter


def tse_api():
    return athena_api('tse')


def candidatos_api():
    return athena_api('candidatos')


def legendas_api():
    return athena_api('legendas')


def votos_api():
    return athena_api('votos')


def athena_api(table):
    lang(request.args.get('lang', 'pt'))

    options = AthenaQueryOptions(table).to_dict()
    track_event("API", options['name'])

    return _athena_response(options, wait=True)


def athena_query_api():
    lang(request.args.get('lang', 'pt'))

    query = AthenaQuery()
    options = AthenaQueryOptions()
    track_event("API", options.name)

    return jsonify(query.get_info(options.to_dict()))


def athena_status_api():
    lang(request.args.get('lang', 'pt'))

    query = AthenaQuery()
    options = AthenaResultOptions()
    options.validate()

    return jsonify(query.get_status(options.to_dict()))


def athena_result_api():
    lang(request.args.get('lang', 'pt'))

    options = AthenaResultOptions()
    options.validate()
    return _athena_response(options.to_dict())


def _athena_response(options, wait=False):
    _validate_api_version()

    try:
        query = AthenaQuery()
        info = query.get_info(options)
        converter = ResponseConverter(info['name'])

        if options['length'] > 0:
            df = query.get_df(options, wait)
            if options['format'] == 'json':
                return converter.to_json(df)
            else:
                return converter.to_csv(df, options['separator'])
        else:
            stream = query.get_stream(options, wait)
            return converter.to_stream(stream)

    except ClientError as e:
        raise BadRequest(str(e))
    except AthenaQueryFailed as e:
        raise BadRequest(str(e))
    except QueryNotFoundException as e:
        raise NotFound(str(e))


def _validate_api_version():
    py_ver = request.args.get('py_ver')
    r_ver = request.args.get('r_ver')

    if py_ver and py_ver != '*' and py_ver != API_PYTHON_VERSION:
        raise BadRequest('Invalid API Version. Please, update your python api library to the latest version.')

    if r_ver and r_ver != '*' and r_ver != API_R_VERSION:
        raise BadRequest('Invalid API Version. Please, update your R api library to the latest version.')
