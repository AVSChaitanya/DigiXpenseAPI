#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from fastapi import Depends
from sqlalchemy import URL
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from typing_extensions import Annotated

from DigiXpenseAPI.app.common.log import log
from DigiXpenseAPI.app.core.conf import settings
from DigiXpenseAPI.app.models.base import MappedBase


def create_engine_and_session(url: str | URL):
    try:
        # Database engine
        engine = create_async_engine(url, echo=settings.DB_ECHO, future=True, pool_pre_ping=True)
        # log.success('Database connection successful')
    except Exception as e:
        log.error('❌ Database link failed {}', e)
        sys.exit()
    else:
        db_session = async_sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)
        return engine, db_session


SQLALCHEMY_DATABASE_URL = (
    f'postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:'
    f'{settings.DB_PORT}/{settings.DB_DATABASE}?charset={settings.DB_CHARSET}'
)

async_engine, async_db_session = create_engine_and_session(SQLALCHEMY_DATABASE_URL)


async def get_db() -> AsyncSession:
    """session Builder"""
    session = async_db_session()
    try:
        yield session
    except Exception as se:
        await session.rollback()
        raise se
    finally:
        await session.close()


# Session Annotated
CurrentSession = Annotated[AsyncSession, Depends(get_db)]


async def create_table():
    """Create database table"""
    async with async_engine.begin() as coon:
        await coon.run_sync(MappedBase.metadata.create_all)
