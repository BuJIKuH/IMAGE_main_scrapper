from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, String, BigInteger, SmallInteger, Boolean, DateTime
from sqlalchemy.dialects.postgresql import JSONB
import datetime
from database.connect_db import DB_PATH
from sqlalchemy import create_engine


DeclBase = declarative_base()

class Ageless(DeclBase):
    __tablename__ = 'ageless'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(String)
    description = Column(Text)
    url_img = Column(String)
    add_card = Column(String)

class Aksessury_image(DeclBase):
    __tablename__ = 'aksessury_image'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(String)
    description = Column(Text)
    url_img = Column(String)
    add_card = Column(String)


class Bioslimming(DeclBase):
    __tablename__ = 'bioslimming'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(String)
    description = Column(Text)
    url_img = Column(String)
    add_card = Column(String)


class Clear_cell(DeclBase):
    __tablename__ = 'clear_cell'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(String)
    description = Column(Text)
    url_img = Column(String)
    add_card = Column(String)


class Ibeauty(DeclBase):
    __tablename__ = 'ibeauty'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(String)
    description = Column(Text)
    url_img = Column(String)
    add_card = Column(String)


class Iluma(DeclBase):
    __tablename__ = 'iluma'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(String)
    description = Column(Text)
    url_img = Column(String)
    add_card = Column(String)


class Image_md(DeclBase):
    __tablename__ = 'image_md'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(String)
    description = Column(Text)
    url_img = Column(String)
    add_card = Column(String)


class Imask(DeclBase):
    __tablename__ = 'imask'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(String)
    description = Column(Text)
    url_img = Column(String)
    add_card = Column(String)


class Irescue(DeclBase):
    __tablename__ = 'irescue'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(String)
    description = Column(Text)
    url_img = Column(String)
    add_card = Column(String)


class Itrial(DeclBase):
    __tablename__ = 'itrial'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(String)
    description = Column(Text)
    url_img = Column(String)
    add_card = Column(String)


class Nabory_image(DeclBase):
    __tablename__ = 'nabory_image'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(String)
    description = Column(Text)
    url_img = Column(String)
    add_card = Column(String)


class O2_lift(DeclBase):
    __tablename__ = 'o2_lift'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(String)
    description = Column(Text)
    url_img = Column(String)
    add_card = Column(String)


class Ormedic(DeclBase):
    __tablename__ = 'ormedic'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(String)
    description = Column(Text)
    url_img = Column(String)
    add_card = Column(String)


class Prevention(DeclBase):
    __tablename__ = 'prevention'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(String)
    description = Column(Text)
    url_img = Column(String)
    add_card = Column(String)


class The_max(DeclBase):
    __tablename__ = 'the_max'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(String)
    description = Column(Text)
    url_img = Column(String)
    add_card = Column(String)


class Vital_c(DeclBase):
    __tablename__ = 'vital'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(String)
    description = Column(Text)
    url_img = Column(String)
    add_card = Column(String)

if __name__ == '__main__':

    engine = create_engine(DB_PATH)
    SessionClass = sessionmaker(bind=engine)
    db_session = SessionClass()
    DeclBase.metadata.create_all(engine)
    db_session.commit()

