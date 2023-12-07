#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import Request

from DigiXpenseAPI.app.common.exception import errors
from DigiXpenseAPI.app.core.conf import settings


async def demo_site(request: Request):
    """Demo site"""

    method = request.method
    path = request.url.path
    if (
        settings.DEMO_MODE
        and method != 'GET'
        and method != 'OPTIONS'
        and (method, path) not in settings.DEMO_MODE_EXCLUDE
    ):
        raise errors.ForbiddenError(msg='This operation is prohibited in the demo environment')
