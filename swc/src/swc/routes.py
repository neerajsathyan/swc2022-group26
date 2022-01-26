from __future__ import absolute_import
from apis.model import ModelHandler
from web import *


def init_route(app, api):
    """
    It initializes url router(i.e registers urls and apis/views).

    :param app:
    :type app: object
    :param api: API object of an application.
    :type api: object

    :returns: None.
    :rtype: None
    """
    # api key resource routing
    api.add_resource(ModelHandler, '/api')

    # Web routes registration
    app.register_blueprint(web_routes)

    @app.errorhandler(404)
    def page_not_found(e):
        return "Error!", 404
