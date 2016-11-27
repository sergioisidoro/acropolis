# -*- coding: utf-8 -*-
"""Token models."""
import datetime as dt

from acropolis.database import Column, Model, SurrogatePK, db, reference_col, relationship


class Token(Model):
    """A token is a code that transits a secure verification channel."""

    __tablename__ = 'tokens'
    token = Column(db.String(128), unique=True, nullable=False)
    active = Column(db.Boolean(), default=False)

    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    user = relationship('User', backref='tokens')
