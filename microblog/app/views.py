from flask import render_template, flash, redirect 
from microblog.app import apps
from .forms import LoginForm
# for the index page
@apps.route('/')
@apps.route('/index')
def index():
    user = {'nickname':'naibor'} #fake user
    posts = [
        {
            'author':{'nickname':'john'},
            'body': 'wow wonderful day'
        },
        {
            'author':{'nickname':'susa'},
            'body':'great speech'
        }
    ]

    return render_template('index.html',
                            title= 'home',
                            user= user, 
                            posts= posts 
                        )
# for the login page
@apps.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash ('Login requested for OpenID="%s", remember_me =%s' %
        (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template (
        'login.html',
        title ='Sign In',
        form=form,
        providers=apps.config['OPENID_PROVIDERS']
        # the above gets from the config.py a listing of the available openid providers
    )
