from flask_wtf 			import Form
from wtforms   			import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
	url 	= StringField("url", validators=[DataRequired()])
	file 	= StringField("file", validators=[DataRequired()])

