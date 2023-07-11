from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api, Resource
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Initialize Flask-RestX API
api = Api(app, version='1.0', title='Task Management API', description='API endpoints for managing tasks')

# Configure the SQLAlchemy database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:rawad.18@localhost:5432/task_manager'

# Initialize SQLAlchemy and database migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Configure Swagger UI
SWAGGER_URL = '/swagger'
API_URL = '/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Task Management API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.Text)
    completed = db.Column(db.Boolean, default=False)
    priority = db.Column(db.String(50), default='low')
    due_date = db.Column(db.Date)
    category = db.Column(db.String(50))

    def __init__(self, title, description, priority, due_date, category):
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.category = category


@api.route('/tasks')
class TasksResource(Resource):
    def get(self):
        tasks = Task.query.all()
        result = []
        for task in tasks:
            result.append({
                'id': task.id,
                'title': task.title,
                'description': task.description,
                'completed': task.completed,
                'priority': task.priority,
                'due_date': task.due_date,
                'category': task.category
            })
        return jsonify(result)

    def post(self):
        data = request.get_json()
        title = data.get('title')
        description = data.get('description')
        priority = data.get('priority')
        due_date = data.get('due_date')
        category = data.get('category')

        task = Task(title=title, description=description, priority=priority, due_date=due_date, category=category)
        db.session.add(task)
        db.session.commit()
        return jsonify({'message': 'Task created successfully'})


@api.route('/tasks/<int:task_id>')
class TaskResource(Resource):
    def get(self, task_id):
        task = Task.query.get(task_id)
        if task:
            result = {
                'id': task.id,
                'title': task.title,
                'description': task.description,
                'completed': task.completed,
                'priority': task.priority,
                'due_date': task.due_date,
                'category': task.category
            }
            return jsonify(result)
        else:
            return jsonify({'message': 'Task not found'}), 404

    def put(self, task_id):
        task = Task.query.get(task_id)
        if not task:
            return jsonify({'error': 'Task not found'})

        data = request.get_json()
        if 'title' in data:
            task.title = data['title']
        if 'description' in data:
            task.description = data['description']
        if 'completed' in data:
            task.completed = data['completed']
        if 'priority' in data:
            task.priority = data['priority']
        if 'due_date' in data:
            task.due_date = data['due_date']
        if 'category' in data:
            task.category = data['category']

        db.session.commit()
        return jsonify({'message': 'Task updated successfully'})

    def delete(self, task_id):
        task = Task.query.get(task_id)
        if not task:
            return jsonify({'message': 'Task not found'}), 404

        db.session.delete(task)
        db.session.commit()

        return jsonify({'message': 'Task deleted successfully'}), 200


if __name__ == '__main__':
    app.run(debug=True)
