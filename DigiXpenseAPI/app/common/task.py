# !/usr/bin/env python3
# -*- coding: utf-8 -*-
from apscheduler.executors.asyncio import AsyncIOExecutor
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from DigiXpenseAPI.app.common.log import log
from DigiXpenseAPI.app.core.conf import settings


def _scheduler_conf() -> dict:
    """
    task conf

    :return:
    """
    redis_conf = {
        'host': settings.APS_REDIS_HOST,
        'port': settings.APS_REDIS_PORT,
        'password': settings.APS_REDIS_PASSWORD,
        'db': settings.APS_REDIS_DATABASE,
        'socket_timeout': settings.APS_REDIS_TIMEOUT,
    }

    end_conf = {
        # configuration memory
        'jobstores': {'default': RedisJobStore(**redis_conf)},
        # Configure the executor
        'executors': {
            'default': AsyncIOExecutor(),
        },
        # Default parameters when creating a task
        'job_defaults': {
            'coalesce': settings.APS_COALESCE,
            'max_instances': settings.APS_MAX_INSTANCES,
            'misfire_grace_time': settings.APS_MISFIRE_GRACE_TIME,
        },
        # Time zone
        'timezone': settings.DATETIME_TIMEZONE,
    }

    return end_conf


class Scheduler(AsyncIOScheduler):
    def start(self, paused: bool = False):
        try:
            super().start(paused)
        except Exception as e:
            log.error(f'❌ Task scheduler startup failed: {e}')

    def shutdown(self, wait: bool = True):
        try:
            super().shutdown(wait)
        except Exception as e:
            log.error(f'❌ Task scheduler shutdown failed: {e}')


# scheduler
scheduler = Scheduler(**_scheduler_conf())
