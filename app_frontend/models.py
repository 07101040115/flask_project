# coding: utf-8
from sqlalchemy import Column, Date, DateTime, Index, Integer, Numeric, String, text
from database import db


Base = db.Model
metadata = Base.metadata


def to_dict(self):
    """
    model 对象转 字典
    model_obj.to_dict()
    """
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

Base.to_dict = to_dict


class Admin(Base):
    __tablename__ = 'admin'

    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False, server_default=text("''"))
    password = Column(String(60), nullable=False, server_default=text("''"))
    area_code = Column(String(4), nullable=False, server_default=text("''"))
    phone = Column(String(20), nullable=False, server_default=text("''"))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    last_login_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    last_ip = Column(String(20), nullable=False, server_default=text("''"))


class ApplyGet(Base):
    __tablename__ = 'apply_get'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False, index=True)
    type_apply = Column(Integer, nullable=False, server_default=text("'0'"))
    money_apply = Column(Numeric(8, 2), nullable=False, server_default=text("'0.00'"))
    status_apply = Column(Integer, nullable=False, server_default=text("'0'"))
    status_order = Column(Integer, nullable=False, server_default=text("'0'"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    delete_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))


class ApplyPut(Base):
    __tablename__ = 'apply_put'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False, index=True)
    type_apply = Column(Integer, nullable=False, server_default=text("'0'"))
    money_apply = Column(Numeric(8, 2), nullable=False, server_default=text("'0.00'"))
    status_apply = Column(Integer, nullable=False, server_default=text("'0'"))
    status_order = Column(Integer, nullable=False, server_default=text("'0'"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    delete_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))


class AreaCode(Base):
    __tablename__ = 'area_code'

    id = Column(Integer, primary_key=True)
    short_code = Column(String(2), nullable=False, server_default=text("''"))
    area_code = Column(String(4), nullable=False, server_default=text("''"))
    phone_pre = Column(String(7), nullable=False, server_default=text("''"))
    name_c = Column(String(20), nullable=False, server_default=text("''"))
    name_e = Column(String(20), nullable=False, server_default=text("''"))
    country_area = Column(String(20), nullable=False, server_default=text("''"))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Feedback(Base):
    __tablename__ = 'feedback'

    id = Column(Integer, primary_key=True)
    send_user_id = Column(Integer, nullable=False, index=True)
    reply_admin_id = Column(Integer, nullable=False, index=True)
    username = Column(String(512), nullable=False, server_default=text("''"))
    password = Column(String(512), nullable=False, server_default=text("''"))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    reply_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))


class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
    apply_put_id = Column(Integer, nullable=False, index=True)
    apply_get_id = Column(Integer, nullable=False, index=True)
    apply_put_uid = Column(Integer, nullable=False, index=True)
    apply_get_uid = Column(Integer, nullable=False, index=True)
    ticket_put_id = Column(Integer, nullable=False, index=True)
    ticket_get_id = Column(Integer, nullable=False, index=True)
    type = Column(Integer, nullable=False, server_default=text("'0'"))
    money = Column(Numeric(8, 2), nullable=False, server_default=text("'0.00'"))
    status_audit = Column(Integer, nullable=False, server_default=text("'0'"))
    status_pay = Column(Integer, nullable=False, server_default=text("'0'"))
    status_rec = Column(Integer, nullable=False, server_default=text("'0'"))
    audit_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    pay_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    receipt_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Score(Base):
    __tablename__ = 'score'

    user_id = Column(Integer, primary_key=True)
    amount = Column(Numeric(10, 0), nullable=False, server_default=text("'0'"))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class ScoreItem(Base):
    __tablename__ = 'score_item'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False, index=True)
    type = Column(Integer, nullable=False, server_default=text("'0'"))
    score = Column(Numeric(8, 0), nullable=False, server_default=text("'0'"))
    note = Column(String(256), nullable=False, server_default=text("''"))
    status = Column(Integer, nullable=False, server_default=text("'0'"))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class TicketGet(Base):
    __tablename__ = 'ticket_get'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False, index=True)
    apply_get_id = Column(Integer, nullable=False, index=True)
    money = Column(Numeric(8, 2), nullable=False, server_default=text("'0.00'"))
    status_pay = Column(Integer, nullable=False, server_default=text("'0'"))
    receipt_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class TicketPut(Base):
    __tablename__ = 'ticket_put'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False, index=True)
    apply_put_id = Column(Integer, nullable=False, index=True)
    money = Column(Numeric(8, 2), nullable=False, server_default=text("'0.00'"))
    status_pay = Column(Integer, nullable=False, server_default=text("'0'"))
    pay_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class User(Base):
    __tablename__ = 'user'
    __table_args__ = (
        Index('area_code', 'area_code', 'phone', unique=True),
    )

    id = Column(Integer, primary_key=True)
    nickname = Column(String(20), nullable=False, server_default=text("''"))
    avatar_url = Column(String(60), nullable=False, server_default=text("''"))
    email = Column(String(60), nullable=False, server_default=text("''"))
    area_code = Column(String(4), nullable=False, server_default=text("''"))
    phone = Column(String(20), nullable=False, server_default=text("''"))
    birthday = Column(Date, nullable=False, server_default=text("'0000-00-00'"))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    last_ip = Column(String(20), nullable=False, server_default=text("''"))


class UserAuth(Base):
    __tablename__ = 'user_auth'
    __table_args__ = (
        Index('auth_type', 'auth_type', 'auth_key', unique=True),
    )

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    auth_type = Column(Integer, nullable=False, server_default=text("'0'"))
    auth_key = Column(String(60), nullable=False, server_default=text("''"))
    auth_secret = Column(String(60), nullable=False, server_default=text("''"))
    status_verified = Column(Integer, nullable=False, server_default=text("'0'"))
    status_lock = Column(Integer, nullable=False, server_default=text("'0'"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class UserBank(Base):
    __tablename__ = 'user_bank'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False, index=True)
    id_card = Column(String(32), nullable=False, server_default=text("''"))
    account_name = Column(String(60), nullable=False, server_default=text("'0'"))
    bank_name = Column(String(60), nullable=False, server_default=text("''"))
    bank_address = Column(String(60), nullable=False, server_default=text("''"))
    bank_account = Column(String(32), nullable=False, server_default=text("''"))
    status_verified = Column(Integer, nullable=False, server_default=text("'0'"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Wallet(Base):
    __tablename__ = 'wallet'

    user_id = Column(Integer, primary_key=True)
    amount_initial = Column(Numeric(10, 2), nullable=False, server_default=text("'0.00'"))
    amount_current = Column(Numeric(10, 2), nullable=False, server_default=text("'0.00'"))
    amount_lock = Column(Numeric(10, 2), nullable=False, server_default=text("'0.00'"))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class WalletItem(Base):
    __tablename__ = 'wallet_item'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False, index=True)
    type = Column(Integer, nullable=False, server_default=text("'0'"))
    money = Column(Numeric(8, 2), nullable=False, server_default=text("'0.00'"))
    sc_id = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    note = Column(String(256), nullable=False, server_default=text("''"))
    status = Column(Integer, nullable=False, server_default=text("'0'"))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))