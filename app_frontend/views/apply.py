#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: apply.py
@time: 2017/4/27 上午9:34
"""


from datetime import datetime
from flask import redirect
from flask import render_template, request, flash, g
from flask import url_for
from flask_login import current_user, login_required

from app_frontend import app
from app_frontend.models import User
from app_frontend.api.apply_get import get_apply_get_rows, get_apply_get_row
from app_frontend.api.apply_put import get_apply_put_rows, get_apply_put_row
from app_api.maps.status_order import *
from flask import Blueprint


bp_apply = Blueprint('apply', __name__, url_prefix='/apply')


@bp_apply.route('/put/list/')
@bp_apply.route('/put/list/<int:page>/')
@login_required
def lists_put(page=1):
    """
    投资申请列表
    """
    uid = current_user.id
    condition = {
        'user_id': uid,
        'status_order': 0,
        'status_delete': 0
    }
    # 订单状态
    status_order = request.args.get('status_order', 0, type=int)
    if status_order in STATUS_ORDER_DICT:
        condition['status_order'] = status_order

    pagination = get_apply_put_rows(page, **condition)
    return render_template('apply/put_list.html', title='apply_put_list', pagination=pagination)


@bp_apply.route('/get/list/')
@bp_apply.route('/get/list/<int:page>/')
@login_required
def lists_get(page=1):
    """
    提现申请列表
    """
    uid = current_user.id
    condition = {
        'user_id': uid,
        'status_order': 0,
        'status_delete': 0
    }
    # 订单状态
    status_order = request.args.get('status_order', 0, type=int)
    if status_order in STATUS_ORDER_DICT:
        condition['status_order'] = status_order

    pagination = get_apply_get_rows(page, **condition)
    return render_template('apply/get_list.html', title='apply_get_list', pagination=pagination)


@bp_apply.route('/put/add/', methods=['GET', 'POST'])
@login_required
def add_put():
    """
    创建投资申请
    :return:
    """
    pass


@bp_apply.route('/get/add/', methods=['GET', 'POST'])
@login_required
def add_get():
    """
    创建提现申请
    :return:
    """
    pass


@bp_apply.route('/put/del/', methods=['GET', 'POST'])
@login_required
def delete_put():
    """
    删除投资申请
    :return:
    """
    pass


@bp_apply.route('/get/del/', methods=['GET', 'POST'])
@login_required
def delete_get():
    """
    删除提现申请
    :return:
    """
    pass


@bp_apply.route('/put/stats/', methods=['GET', 'POST'])
@login_required
def stats_put():
    """
    投资申请统计
    :return:
    """
    pass


@bp_apply.route('/get/stats/', methods=['GET', 'POST'])
@login_required
def stats_get():
    """
    提现申请统计
    :return:
    """
    pass
