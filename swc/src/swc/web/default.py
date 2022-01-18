from . import web_routes


@web_routes.route('/', methods=["GET"])
def login():
    return "Welcome to SWC Project"
