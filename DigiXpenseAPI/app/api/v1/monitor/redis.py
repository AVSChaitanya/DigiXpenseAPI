#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import APIRouter

#from SocialAnalytics.app.common.jwt import DependsJwtAuth
from app.common.response.response_schema import response_base
from app.utils.redis_info import redis_info

router = APIRouter()


@router.get('/redis', summary='redis monitor', dependencies=[DependsJwtAuth])
async def get_redis_info():
    data = {'info': await redis_info.get_info(), 'stats': await redis_info.get_stats()}
    return await response_base.success(data=data)
