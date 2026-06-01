import os
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = ''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Task(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'content': self.content
        }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/tasks', methods=['GET'])
def get_tasks():

    try:
        tasks = Task.query.all()

        return jsonify([task.to_dict() for task in tasks])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/add', methods=['POST'])
def add_task():
    try:
        data = request.get_json()
        if not data or 'content' not in data:
            return jsonify({'error': 'Missing task content'}), 400
            
        new_task = Task(content=data['content'])
        db.session.add(new_task)
        db.session.commit()
        
        return jsonify(new_task.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/delete/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    try:
        task_to_delete = Task.query.get(task_id)
        
        if task_to_delete is None:
            return jsonify({'error': 'Task not found'}), 404
            
        db.session.delete(task_to_delete)
        db.session.commit()
        
        return jsonify({'message': 'Task deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
