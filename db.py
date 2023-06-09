from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine
from config import host, user, password, db_name, port
from sqlalchemy.orm import sessionmaker

try:
    url = f'postgresql://{user}:{password}@{host}:{port}/{db_name}'
    if not database_exists(url):
        create_database(url)

    engine = create_engine(url, pool_size=50, echo=True)

    Session = sessionmaker(bind=engine)
    session = Session()

except Exception as ex:
    print('Something gone wrong with PostgreSQL', ex)

finally:
    print('PostgreSQL connection closed')
