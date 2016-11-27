# -*- coding: utf-8 -*-
"""Address models."""
import datetime as dt

from acropolis.database import Column, Model, SurrogatePK, db, reference_col, relationship

class SpaceUnit(Model):
    __tablename__ = 'cities'
    code = Column(db.String(128), unique=True, nullable=False)


class Address(Model):
    """An address is a junction of all subdivisions of itself"""
    pass

class City(SpaceUnit):
    """A City, it it's broad sense."""

    __tablename__ = 'cities'
    name = Column(db.String(128), unique=True, nullable=False)


class District(SpaceUnit):
    """A District is a sub division of a city."""
    __tablename__ = 'districts'
    name = Column(db.String(128), unique=True, nullable=False)


class Street(SpaceUnit):
    """A Street is a Street."""

    __tablename__ = 'streets'
    name = Column(db.String(128), unique=False, nullable=False)


class Block(SpaceUnit):
    """A block is a gathering of buildings"""

    __tablename__ = 'blocks'
    name = Column(db.String(128), unique=False, nullable=False)


class Building(SpaceUnit):
    """A Building is an individual phisical strucuture."""

    __tablename__ = 'buildings'
    name = Column(db.String(128), unique=False, nullable=False)


class Stairwell(SpaceUnit):
    """A stairwell is a separate entrance to a certain building"""

    __tablename__ = 'stairwells'
    name = Column(db.String(128), unique=False, nullable=False)


class Floor(SpaceUnit):
    """A floor is a same leveled surface of a building"""

    __tablename__ = 'floors'
    name = Column(db.String(128), unique=False, nullable=False)


class Appartment(SpaceUnit):
    """An appartment is single unit of living, non communal"""

    __tablename__ = 'appartments'
    name = Column(db.String(128), unique=False, nullable=False)
