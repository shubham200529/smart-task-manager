import pandas as pd

import numpy as np

from app.models import Task


def get_task_analytics(user_id):

    tasks = Task.query.filter_by(user_id=user_id).all()

    task_list = []

    for task in tasks:

        task_list.append({
            'title': task.title,
            'status': task.status
        })

    if len(task_list) == 0:

        return {
            'total_tasks': 0,
            'completed_tasks': 0,
            'pending_tasks': 0,
            'completion_percentage': 0
        }

    df = pd.DataFrame(task_list)

    total_tasks = len(df)

    completed_tasks = df[
        df['status'] == 'Completed'
    ].shape[0]

    pending_tasks = df[
        df['status'] == 'Pending'
    ].shape[0]

    completion_percentage = np.round(
        (completed_tasks / total_tasks) * 100,
        2
    )

    return {
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'completion_percentage': completion_percentage
    }