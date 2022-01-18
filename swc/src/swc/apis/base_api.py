import traceback

from flask import current_app
from flask_restful import Resource
from flask_restful import request


class BaseResource(Resource):
    """
    Base class of handlers.
    """

    def __init__(self):
        current_app.logger.info('Base resource initialized.')
        current_app.api_version = "v1"
        self.__status = True
        # Status message of last executed function
        self.__status_msg = ''
        # Search params

        # List of sentences
        self.sentences = None
        # Collection name in response
        self.__collection_name = 'resources'

    # status getter and setter
    @property
    def status(self):
        """Status getter method."""
        return self.__status

    @status.setter
    def status(self, value):
        """Status setter method."""
        self.__status = value

    # status_msg getter and setter
    @property
    def status_message(self):
        """Status message getter method."""
        return self.__status_msg

    @status_message.setter
    def status_message(self, value):
        """Status message setter method."""
        self.__status_msg = value

    def get_data(self, check_none=True):
        """
        It gets requests post/patch json data and verifies with respective model
        schema.

        :param check_none: If True then checks request data for None. Default True.
        :type check_none: bool

        :return: It returns result of request data processing true/false and request data.
        :rtype: tuple
        """
        data = {}
        try:
            data = request.get_json()
        except:
            pass

        if check_none and not data:
            current_app.logger.error('Validation failed. \
            Field params not provided')
            self.status = 400
            self.status_message = "Validation Failed."
            return False, None
        else:
            # TODO Field by field validation
            pass

        return True, data

    def get_url_data(self):
        """
        It gets request's url query data and verifies with respective model
        schema.

        :return: It returns result of request data processing true/false and request data.
        :rtype: tuple
        """
        data = {}
        try:
            data = request.args
            if data:
                data = dict((k, v) for k, v in list(data.items()))
            else:
                data = {}
        except:
            pass
            # traceback.print_exc()

        return True, data

    def response_error(self, status=None, msg=None):
        """
        Returns HTTP input status response with message.

        :param status: HTTP response status code.
        :type status: int
        :param msg: Response message.
        :type msg: string

        :return: Json object includs response message and HTTP status response.
        :rtype: tuple
        """
        if not status:
            status = self.status

        if not msg:
            msg = self.status_message

        # Set response
        return {
                   'status': status,
                   'messages': msg
               }, status

    def response_200(self, obj):
        return obj, 200

    def response_201(self, obj):
        """
        Returns HTTP 201 status response with input object.

        :param obj:colln json object in response.
        :type obj: dictionary

        :return: Json object and HTTP status 201 response.
        :rtype: tuple
        """
        # Set response
        return obj, 201

    def response_409(self, obj):
        """
        Returns HTTP 201 status response with input object.

        :param obj:colln json object in response.
        :type obj: dictionary

        :return: Json object and HTTP status 201 response.
        :rtype: tuple
        """
        # Set response
        return {"resource": obj, "status": 409, "message": self.status_message}, 409

    def error_404(self):
        return {
                   'status': 404,
                   'messages': "Not found"
               }, 404

    def get(self, id=None):
        return self.error_404()

    def post(self):
        return self.error_404()

    def put(self, id=None):
        return self.error_404()

    def patch(self, id=None):
        return self.error_404()

    def delete(self, id=None):
        return self.error_404()


class BaseHandler(BaseResource):
    """
    Base class of single object handlers.
    """

    def __init__(self):
        current_app.logger.info('Base handler initialized.')
        BaseResource.__init__(self)
        self.__pk_param_name = 'id'


class BaseListHandler(BaseResource):
    """
    Base class of list handlers.
    """

    def __init__(self):
        current_app.logger.info('Base list handler initialized.')
        BaseResource.__init__(self)
