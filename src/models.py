import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    email = Column(String(150), unique=True, nullable=False)
    user_name = Column(String(30), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    first_name = Column(String(50), nullable=True)
    address_1 = Column(String(150), nullable=True)
    address_2 = Column(String(150), nullable=True)
    
    character_favourites = relationship("CharacterFavourites", back_populates="user")
    planet_favourites = relationship("PlanetFavourites", back_populates="user")
    spaceship_favourites = relationship("SpaceshipFavourites", back_populates="user")
    vehicle_favourites = relationship("VehicleFavourites", back_populates="user")

class Characters(Base):
    __tablename__ = 'characters'
    character_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    species = Column(String(30), nullable=True)
    gender = Column(String(10), nullable=True)
    age = Column(Integer, nullable=True)
    weight = Column(Integer, nullable=True)
    height = Column(Integer, nullable=True)

    favourites = relationship("CharacterFavourites", back_populates="character")

class Spaceships(Base):
    __tablename__ = 'spaceships'
    spaceship_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    spaceshipClass = Column(String(30), nullable=True)
    model = Column(String(50), nullable=True)
    passengers = Column(Integer, nullable=True)
    loadcapacity = Column(Integer, nullable=True)
    size = Column(Integer, nullable=True)

    favourites = relationship("SpaceshipFavourites", back_populates="spaceship")

class Planets(Base):
    __tablename__ = 'planets'
    planet_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    population = Column(Integer, nullable=True)
    diameter = Column(Integer, nullable=True)
    orbitalPeriod = Column(Integer, nullable=True)
    climate = Column(String(50), nullable=True)

    favourites = relationship("PlanetFavourites", back_populates="planet")

class Vehicles(Base):
    __tablename__ = 'vehicles'
    vehicle_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    vehicleClass = Column(String(30), nullable=True)
    model = Column(String(50), nullable=True)
    passengers = Column(Integer, nullable=True)
    loadcapacity = Column(Integer, nullable=True)
    size = Column(Integer, nullable=True)

    favourites = relationship("VehicleFavourites", back_populates="vehicle")

class CharacterFavourites(Base):
    __tablename__ = 'character_favourites'
    favourites_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    character_id = Column(Integer, ForeignKey('characters.character_id'), nullable=False)

    user = relationship("User", back_populates="character_favourites")
    character = relationship("Characters", back_populates="favourites")

class PlanetFavourites(Base):
    __tablename__ = 'planet_favourites'
    favourites_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planets.planet_id'), nullable=False)

    user = relationship("User", back_populates="planet_favourites")
    planet = relationship("Planets", back_populates="favourites")

class SpaceshipFavourites(Base):
    __tablename__ = 'spaceship_favourites'
    favourites_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    spaceship_id = Column(Integer, ForeignKey('spaceships.spaceship_id'), nullable=False)

    user = relationship("User", back_populates="spaceship_favourites")
    spaceship = relationship("Spaceships", back_populates="favourites")

class VehicleFavourites(Base):
    __tablename__ = 'vehicle_favourites'
    favourites_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    vehicle_id = Column(Integer, ForeignKey('vehicles.vehicle_id'), nullable=False)

    user = relationship("User", back_populates="vehicle_favourites")
    vehicle = relationship("Vehicles", back_populates="favourites")

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

