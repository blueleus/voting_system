import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from voting_system.db import get_db

bp = Blueprint('question', __name__, url_prefix='/question')


@bp.route('/')
def index():
    db = get_db()
    questions = db.execute('SELECT * FROM question ORDER BY created DESC').fetchall()
    return render_template('question/index.html', questions=questions)


@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        text = request.form['text']
        error = None

        if not text:
            error = 'Question\'s text is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute('INSERT INTO question (text) VALUES (?)', (text,))
            db.commit()
            return redirect(url_for('question.index'))

    return render_template('question/create.html')