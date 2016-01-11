#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Models for user, blog, comment,api.
'''

__author__ = 'Denny Shi'

import time, uuid

from orm import Model, StringField, BooleanField, FloatField, TextField

def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

class Bills(Model):
    __table__ = 'bills'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    service_name = StringField(ddl='varchar(300)')
    services = []
    service_id = StringField(ddl='varchar(50)')
    enterprise_id = StringField(ddl='varchar(50)')
    customer_name = StringField(ddl='varchar(50)')
    create_time = FloatField(default=time.time)
class Order(Model):
    __table__ = 'order'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    service_name = StringField(ddl='varchar(300)')
    services = []
    service_id = StringField(ddl='varchar(50)')
    order_type = StringField(ddl='varchar(50)')
    enterprise_id = StringField(ddl='varchar(50)')
    customer_name = StringField(ddl='varchar(50)')
    creator = StringField(ddl='varchar(50)')
    project_no = StringField(ddl='varchar(50)')
    create_time = FloatField(default=time.time)
    opening_time = FloatField(default=time.time)
class User(Model):
    __table__ = 'users'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    created_at = FloatField(default=time.time)

class Blog(Model):
    __table__ = 'blogs'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(200)')
    content = TextField()
    created_at = FloatField(default=time.time)

class Comment(Model):
    __table__ = 'comments'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)

class Hospital(Model):
    __table__ = 'hospitals'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    name = StringField(ddl='varchar(50)')
    description = TextField()
    user_name = StringField(ddl='varchar(50)')
    user_password = StringField(ddl='varchar(50)')

class Service(Model):
    __table__= 'services'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    name = StringField(ddl='varchar(50)')
    description = TextField()

class HospitalService(Model):
    __table__= 'hospital_service'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    hospital_id = StringField(ddl='varchar(50)')
    service_id = StringField(ddl='varchar(50)')
