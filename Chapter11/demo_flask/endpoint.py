import flask.views

class Endpoint(flask.views.MethodView):
    def post(self):
        flask.abort(405)

    def get(self, id):
        flask.abort(405)

    def put(self, id):
        flask.abort(405)

    def delete(self, id):
        flask.abort(405)

    @classmethod
    def register(class_, app, base = '', default_id = None):
        view = class_.as_view(class_.__name__)

        # When no ID is provided, accept GET and use the default ID
        app.add_url_rule('{}/{}'.format(base, class_.__name__.lower()),
                         defaults = {'id': default_id},
                         view_func = view,
                         methods = ['GET'])

        # When no ID is provided, accept POST
        app.add_url_rule('{}/{}'.format(base, class_.__name__.lower()),
                         view_func = view,
                         methods = ['POST'])

        # When an ID is provided, accept GET, PUT, and DELETE
        app.add_url_rule('{}/{}/<int:id>'.format(base, class_.__name__.lower()),
                         view_func = view,
                         methods = ['GET', 'PUT', 'DELETE'])

