from flask_restplus import Namespace, Resource, fields

import settings

api = Namespace(settings.ENDPOINT_1, description=settings.ENDPOINT_1_DESCRIPTION)


@api.route(settings.ENDPOINT_1_ROUTE_1)
class Endpoint(Resource):

    def get(self):
        return 'OK'
