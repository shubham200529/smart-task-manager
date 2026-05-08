from flask import Blueprint, jsonify, request

from flask_login import login_required, current_user

from app.models import Task

from app import db, socketio


task_bp = Blueprint('tasks', __name__)


@task_bp.route('/tasks', methods=['GET'])
@login_required
def get_tasks():

    tasks = Task.query.filter_by(
        user_id=current_user.id
    ).all()

    data = []

    for task in tasks:

        data.append({
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'priority': task.priority,
            'status': task.status
        })

    return jsonify(data)


@task_bp.route('/tasks', methods=['POST'])
@login_required
def add_task():

    data = request.json

    task = Task(
        title=data['title'],
        description=data['description'],
        priority=data['priority'],
        status=data['status'],
        user_id=current_user.id
    )

    db.session.add(task)

    db.session.commit()

    socketio.emit(
        'task_update',
        {'message': 'New task added'}
    )

    return jsonify({
        'message': 'Task added successfully'
    })


@task_bp.route('/tasks/<int:id>', methods=['PUT'])
@login_required
def update_task(id):

    task = Task.query.get_or_404(id)

    data = request.json

    task.status = data['status']

    db.session.commit()

    socketio.emit(
        'task_update',
        {'message': 'Task updated'}
    )

    return jsonify({
        'message': 'Task updated successfully'
    })


@task_bp.route('/tasks/<int:id>', methods=['DELETE'])
@login_required
def delete_task(id):

    task = Task.query.get_or_404(id)

    db.session.delete(task)

    db.session.commit()

    socketio.emit(
        'task_update',
        {'message': 'Task deleted'}
    )

    return jsonify({
        'message': 'Task deleted successfully'
    })