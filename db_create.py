from config.db import meta, engine
from models.user import users
meta.create_all(engine,tables=[users])