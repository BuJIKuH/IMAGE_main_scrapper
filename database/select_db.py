from connect_db import create_dbsession
from models_sql import Chemical_catalog


def select_some_col():
    query = 'Нонилфенол'
    db_session = create_dbsession()
    result = db_session.query(Chemical_catalog)
    # result = session.query(Customers).filter(Customers.id > 2)
    for row in result:
        if row.chemical_name == query:
            print(row.id)




if __name__ == '__main__':
    select_some_col()