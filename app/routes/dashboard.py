from flask import Blueprint, render_template

from flask_login import login_required, current_user

from app.analytics import get_task_analytics

from app.models import Task


dashboard_bp = Blueprint('dashboard', __name__)


@dashboard_bp.route('/')
@login_required
def dashboard():

    tasks = Task.query.filter_by(
        user_id=current_user.id
    ).all()

    analytics = get_task_analytics(
        current_user.id
    )

    return render_template(
        'dashboard.html',
        tasks=tasks,
        analytics=analytics
    )