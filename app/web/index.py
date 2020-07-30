from app.web import web
from flask import render_template, request, flash
from app.forms.markdown import MarkDownForm


@web.route('/', methods=['GET', 'POST'])
def index():
    # mkd = '''
    # # header
    # ## header2
    # [picture](http://www.example.com)
    # * 1
    # * 2
    # * 3
    # **bold**
    # '''
    form = MarkDownForm(request.form)
    if request.method == 'POST':
        if form.validate():
            next_url = request.args.get('next')
        else:
            flash('there is sth wrong')
            return render_template('index.html', form=form)
    return render_template('index.html', form=form)
