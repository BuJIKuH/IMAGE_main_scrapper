# from category import *
# from models_sql import *
# from iter_funcs import iter_func
# from iter_models import iter_models
# from connect_db import create_dbsession
#
#
# def insert_in_db():
#     db_session = create_dbsession()
#     db_session.begin()
#     for item in iter_func():
#         db_session.add_all([
#             iter_models()(
#                 name=item[0],
#                 price=item[1],
#                 description=item[2],
#                 url_img=item[3],
#                 add_card=item[4]
#             )
#         ])
#     db_session.commit()
#     db_session.close()
#
# if __name__ == '__main__':
#
#     insert_in_db()
#     # iter_models()