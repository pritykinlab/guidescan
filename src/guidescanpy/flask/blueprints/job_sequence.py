import logging
from flask import Blueprint, jsonify, render_template
from guidescanpy.tasks import app as tasks_app
from guidescanpy.flask.core.utils import job_result


bp = Blueprint("job_sequence", __name__)
logger = logging.getLogger(__name__)


@bp.route("/<job_id>")
@job_result
def job(job_id):
    result = tasks_app.AsyncResult(job_id)
    return render_template("job_sequence.html", result=result)


@bp.route("/status/<job_id>")
def status(job_id):
    res = tasks_app.AsyncResult(job_id)
    return jsonify({"status": res.status})
