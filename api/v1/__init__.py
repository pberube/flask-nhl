from flask_restplus import Api
from flask import Blueprint

from api import current_config
from api.v1.endpoints.nhl import api as nhl_namespace

blueprint_api_v1 = Blueprint('api_v1', __name__)

authorizations = {
    'authorization_key': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'authorization'
    }
}

api_v1 = Api(blueprint_api_v1,
             title="NHL Games Service",
             version="1.0",
             description="NHL Today's Games.",
             authorizations=authorizations,
             security='authorization_key',
             doc='/' if current_config.SWAGGER_ENABLE == '1' else ''
             )

# Add namespace to api
api_v1.add_namespace(nhl_namespace)

