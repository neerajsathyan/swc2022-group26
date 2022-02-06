import json
import uuid

from sqlalchemy.exc import SQLAlchemyError

from .base_api import BaseListHandler
from .psql_models import PlaceTable, PlaceTableSchema

placetable_schema = PlaceTableSchema()


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
                return self.response_200({'uuid': str(uuid.uuid4()), 'places': [json.loads(place.to_json())]})

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
                return self.response_200({'uuid': str(uuid.uuid4()), 'places': [json.loads(place.to_json())]})


class CrudHandler(BaseListHandler):
    def __init__(self):
        self.pk_param_name = 'uuid'
        self.collection = 'places'

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
                return self.response_200({'uuid': str(uuid.uuid4()), 'places': [json.loads(place.to_json())]})

    def post(self):
        # Post method to add a place into the table place_table
        status, data = self.get_data()
        if not status:
            return self.response_error(400, "Invalid Post Data")
        name = data.get("name", '')
        if name is None or name is '':
            # No name is given... then show invalid post data..
            return self.response_error(400, "No name element added")
        else:
            place = PlaceTable(data)
            try:
                place.save()
            except SQLAlchemyError as e:
                error = str(e.__dict__['orig'])
                return self.response_error(400, error)
            return self.response_200({'uuid': str(uuid.uuid4()), 'message': "Successfully inserted the place to db."})

    def put(self):
        # Update field..
        status, data = self.get_data()
        if not status:
            return self.response_error(400, "Invalid request")
        data = placetable_schema.load(data, partial=True)
        try:
            place = PlaceTable.get_one_places(data.get("id"))
        except KeyError as e:
            return self.response_error(400, "Invalid id")
        if place is None:
            return self.response_error(400, "ID not found!")
        try:
            place.update(data)
        except SQLAlchemyError as error2:
            return self.response_error(400, str(error2.__dict__['orig']))
        return self.response_200({'uuid': str(uuid.uuid4()), 'message': "Successfully updated Details!"})

    def delete(self):
        # Delete field..
        status, data = self.get_data()
        if not status:
            return self.response_error(400, "Invalid request")
        data = placetable_schema.load(data, partial=True)
        try:
            place = PlaceTable.get_one_places(data.get("id"))
        except KeyError as e:
            return self.response_error(400, "Invalid id")
        if place is None:
            return self.response_error(400, "ID not found!")
        try:
            place.delete()
        except SQLAlchemyError as error2:
            return self.response_error(400, str(error2.__dict__['orig']))
        return self.response_200({'uuid': str(uuid.uuid4()), 'message': "Successfully deleted Details!"})