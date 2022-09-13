from category import *
from models_sql import *


from connect_db import create_dbsession


def insert_in_db():
    db_session = create_dbsession()
    db_session.begin()
    for item in array_ageless():
        db_session.add_all([
            Ageless(
                name=item[0],
                price=item[1],
                description=item[2],
                url_img=item[3],
                add_card=item[4])])


    for item in array_aksessury_image():
        db_session.add_all([
            Aksessury_image(
                name=item[0],
                price=item[1],
                description=item[2],
                url_img=item[3],
                add_card=item[4])])

    for item in array_bioslimming():
        db_session.add_all([
            Bioslimming(
                name=item[0],
                price=item[1],
                description=item[2],
                url_img=item[3],
                add_card=item[4])])

    for item in array_clear_cell():
        db_session.add_all([
            Clear_cell(
                name=item[0],
                price=item[1],
                description=item[2],
                url_img=item[3],
                add_card=item[4])])

    for item in array_ibeauty():
        db_session.add_all([
            Ibeauty(
                name=item[0],
                price=item[1],
                description=item[2],
                url_img=item[3],
                add_card=item[4])])

    for item in array_iluma():
        db_session.add_all([
            Iluma(
                name=item[0],
                price=item[1],
                description=item[2],
                url_img=item[3],
                add_card=item[4])])

    for item in array_image_md():
        db_session.add_all([
            Image_md(
                name=item[0],
                price=item[1],
                description=item[2],
                url_img=item[3],
                add_card=item[4])])

    for item in array_imask():
        db_session.add_all([
            Imask(
                name=item[0],
                price=item[1],
                description=item[2],
                url_img=item[3],
                add_card=item[4])])

    for item in array_irescue():
        db_session.add_all([
            Irescue(
                name=item[0],
                price=item[1],
                description=item[2],
                url_img=item[3],
                add_card=item[4])])

    for item in array_itrial():
        db_session.add_all([
            Itrial(
                name=item[0],
                price=item[1],
                description=item[2],
                url_img=item[3],
                add_card=item[4])])

    for item in array_nabory_image():
        db_session.add_all([
            Nabory_image(
                name=item[0],
                price=item[1],
                description=item[2],
                url_img=item[3],
                add_card=item[4])])

    for item in array_o2_lift():
        db_session.add_all([
            O2_lift(
                name=item[0],
                price=item[1],
                description=item[2],
                url_img=item[3],
                add_card=item[4])])

    for item in array_ormedic():
        db_session.add_all([
            Ormedic(
                name=item[0],
                price=item[1],
                description=item[2],
                url_img=item[3],
                add_card=item[4])])

    for item in array_prevention():
        db_session.add_all([
            Prevention(
                name=item[0],
                price=item[1],
                description=item[2],
                url_img=item[3],
                add_card=item[4])])

    for item in array_the_max():
        db_session.add_all([
            The_max(
                name=item[0],
                price=item[1],
                description=item[2],
                url_img=item[3],
                add_card=item[4])])

    for item in array_vital_c():
        db_session.add_all([
            Vital_c(
                name=item[0],
                price=item[1],
                description=item[2],
                url_img=item[3],
                add_card=item[4])])


    db_session.commit()
    db_session.close()

if __name__ == '__main__':

    insert_in_db()
    # iter_models()