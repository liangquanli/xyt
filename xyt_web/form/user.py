#!/usr/bin/env python
# encoding: utf-8
from wtforms import Form, StringField, PasswordField, validators


class LoginForm(Form):
    """
    登录表单
    """

    phone = StringField('手机号', [
        validators.DataRequired(message='手机号不能为空')
    ])
    password = PasswordField('密码', [validators.DataRequired(message='密码不能为空')])


class FindPasswordForm(Form):
    """
    找回密码表单
    """

    phone = StringField(
        '手机号',
        [validators.DataRequired(message='手机号不能为空')]
    )
    confirm = StringField(
        '验证码',
        [validators.DataRequired(message='验证码不能为空')]
    )


class ResetPasswordForm(Form):
    """
    重置密码表单
    """

    password = PasswordField('密码', [validators.DataRequired(message='密码不能为空')])
    confirm_password = PasswordField('确认密码', [validators.EqualTo('password', message='两次密码输入需要一致')])


class ChangePasswordForm(Form):
    """
    修改密码表单
    """

    old_password = PasswordField('旧密码', [validators.DataRequired(message='密码不能为空')])
    new_password = PasswordField('新密码', [validators.DataRequired(message='密码不能为空')])
    confirm_password = PasswordField('确认密码', [validators.EqualTo('new_password', message='两次密码输入需要一致')])


class ChangePhoneForm(Form):
    """
    修改手机号表单
    """

    old_phone = StringField('当前手机号', [validators.DataRequired(message='当前手机号不能为空')])
    new_phone = StringField('新手机号', [validators.DataRequired(message='新手机号不能为空')])
    confirm = StringField(
        '验证码',
        [validators.DataRequired(message='验证码不能为空')]
    )