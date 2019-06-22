from extensions import login_mgr

from .main import main # noqa
from .auth import auth # noqa
from .models import User


@login_mgr.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))
