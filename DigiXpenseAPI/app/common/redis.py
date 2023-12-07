#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from redis.asyncio.client import Redis
from redis.exceptions import TimeoutError, AuthenticationError

from DigiXpenseAPI.app.common.log import log
from DigiXpenseAPI.app.core.conf import settings


class RedisCli(Redis):
    def __init__(self):
        super(RedisCli, self).__init__(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            password=settings.REDIS_PASSWORD,
            db=settings.REDIS_DATABASE,
            socket_timeout=settings.REDIS_TIMEOUT,
            decode_responses=True,  # 转码 utf-8
        )

    async def open(self):
        """
        Trigger initial connection

        :return:
        """
        try:
            await self.ping()
        except TimeoutError:
            log.error('❌ Database redis connection timeout')
            sys.exit()
        except AuthenticationError:
            log.error('❌ Database redis connection authentication failed')
            sys.exit()
        except Exception as e:
            log.error('❌ Database redis connection exception {}', e)
            sys.exit()

    async def delete_prefix(self, prefix: str, exclude: str | list = None):
        """
        Delete all keys with the specified prefix

        :param prefix:
        :param exclude:
        :return:
        """
        keys = []
        async for key in self.scan_iter(match=f'{prefix}*'):
            if isinstance(exclude, str):
                if key != exclude:
                    keys.append(key)
            elif isinstance(exclude, list):
                if key not in exclude:
                    keys.append(key)
            else:
                keys.append(key)
        for key in keys:
            await self.delete(key)


# Create redis connection object
redis_client = RedisCli()
