import json
import uuid

from .base_api import BaseListHandler
from .psql_models import PlaceTable


class ModelHandler(BaseListHandler):
    def __init__(self):
        self.pk_param_name = 'id'
        self.collection = 'models'

    def get(self):
        status, data = self.get_url_data()
        data = data.get("id", '')
        if data is None or len(data) == 0:
            # No id given... then display all details..
            places = PlaceTable.query.all()
            if places is None:
                return self.response_error(400, "ID not found!")
            else:
                results = [json.loads(place.to_json()) for place in places]
                response = {'uuid': str(uuid.uuid4()), 'places': results}
                print(response)
                return self.response_200(response)

        else:
            place = PlaceTable.query.get(data)
            if place is None:
                return self.response_error(400, "ID not found!")
            else:
                return self.response_200({'uuid': str(uuid.uuid4()), 'places': json.loads(place.to_json())})

    def post(self):
        status, data = self.get_data()
        if not status:
            places = PlaceTable.query.all()
            if places is None:
                return self.response_error(400, "ID not found!")
            else:
                results = [json.loads(place.to_json()) for place in places]
                response = {'uuid': str(uuid.uuid4()), 'places': results}
                print(response)
                return self.response_200(response)
        id = data.get("id", '')
        if id is None or id is '':
            # No id given... then display all details..
            places = PlaceTable.query.all()
            if places is None:
                return self.response_error(400, "ID not found!")
            else:
                results = [json.loads(place.to_json()) for place in places]
                response = {'uuid': str(uuid.uuid4()), 'places': results}
                print(response)
                return self.response_200(response)
        else:
            place = PlaceTable.query.get(id)
            if place is None:
                return self.response_error(400, "ID not found!")
            else:
                return self.response_200({'uuid': str(uuid.uuid4()), 'places': json.loads(place.to_json())})