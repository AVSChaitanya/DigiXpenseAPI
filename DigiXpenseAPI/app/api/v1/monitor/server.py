#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import APIRouter
from starlette.concurrency import run_in_threadpool

#from SocialAnalytics.app.common.jwt import DependsJwtAuth
from app.common.response.response_schema import response_base
from app.utils.server_info import server_info

router = APIRouter()


@router.get('/server', summary='server monitor', dependencies=[DependsJwtAuth])
async def get_server_info():
    """For IO-intensive tasks, use thread pools to minimize performance loss"""
    data = {
        'cpu': await run_in_threadpool(server_info.get_cpu_info),
        'mem': await run_in_threadpool(server_info.get_mem_info),
        'sys': await run_in_threadpool(server_info.get_sys_info),
        'disk': await run_in_threadpool(server_info.get_disk_info),
        'service': await run_in_threadpool(server_info.get_service_info),
    }
    return await response_base.success(data=data)
