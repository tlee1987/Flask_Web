#!usr/bin/env python3
# -*- coding:utf-8 -*-
from flask import Flask, abort, jsonify, make_response
from flask_restful import Api, Resource, marshal
from flask_restful import reqparse, fields
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()

tasks = [
    {
        'id': 1,
        'title': 'Buy groceries',
        'description': 'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Need to find a good Python tutorial on the web',
        'done': False
    }
]

task_fields = {
    'title': fields.String,
    'description': fields.String,
    'done': fields.Boolean,
    'uri': fields.Url('task')
}

class TaskListAPI(Resource):

    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type = str, required = True,
                                   help = 'No task title provided', location = 'json')
        self.reqparse.add_argument('description', type = str, default = "", location = 'json')
        super(TaskListAPI, self).__init__()

    def get(self):
        """
        :return: {
                "tasks": [
                    {
                        "title": "Buy groceries",
                        "description": "Milk, Cheese, Pizza, Fruit, Tylenol",
                        "done": false,
                        "uri": "/todo/api/v1.0/tasks/1"
                    },
                    {
                        "title": "Learn Python",
                        "description": "Need to find a good Python tutorial on the web",
                        "done": false,
                        "uri": "/todo/api/v1.0/tasks/2"
                    }
                ]
            }
        """
        return {'tasks': marshal(tasks, task_fields)}

    def post(self):
        pass


class TaskAPI(Resource):

    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type = str, location = 'json')
        self.reqparse.add_argument('description', type = str, location = 'json')
        self.reqparse.add_argument('done', type = bool, location = 'json')
        super(TaskAPI, self).__init__()

    def get(self, id):
        task = list(filter(lambda t: t['id'] == id, tasks))
        if len(task) == 0:
            abort(404)
        return {'task': marshal(task[0], task_fields)}


    def put(self, id):
        task = list(filter(lambda t: t['id'] == id, tasks))
        if len(task) == 0:
            abort(404)
        task = task[0]
        args = self.reqparse.parse_args()
        for k, v in args.items():
            if v != None:
                task[k] = v
        return {'task': marshal(task, task_fields)}

    def delete(self, id):
        pass

api.add_resource(TaskListAPI, '/todo/api/v1.0/tasks', endpoint='tasks')
api.add_resource(TaskAPI, '/todo/api/v1.0/tasks/<int:id>', endpoint='task')


@auth.get_password
def get_password(username):
    if username == 'litian':
        return 'python'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)


if __name__ == '__main__':
    app.run(debug=True)