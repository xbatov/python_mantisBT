from model.project import Project
import string
import random

def random_name(maxlen):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_status():
    values = ["development", "release", "stable", "obsolete"]
    return "".join(random.choice(values))

def random_view_state():
    values = ["public", "private"]
    return "".join(random.choice(values))

def random_description(maxlen):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata =  [
    Project(name=random_name(10), status=random_status(), view_state=random_view_state(), description=random_description(50)),
            ]