#coding:UTF-8
__author__ = 'dj'

from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms.validators import DataRequired, AnyOf
from wtforms import StringField,TextField


class Upload(FlaskForm):
	reportrange = FileField('timesrange', validators=[DataRequired()])


#协议过滤表单
class ProtoFilter(FlaskForm):
    value = FileField('value')
    filter_type = FileField('filter_type', validators=[DataRequired(), AnyOf([u'all', u'proto', u'ipsrc', u'ipdst'])])
#上传用户名密码
class User_and_pwd(FlaskForm):
	username = FileField('username', validators=[DataRequired()])
	password = FileField('password', validators=[DataRequired()])