#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime

from fastapi import APIRouter, File, UploadFile, Form

from app.common.response.response_schema import response_base
from app.common.task import scheduler

router = APIRouter(prefix='/tests')


def task_demo():
    print('Common tasks')


async def task_demo_async():
    print('Asynchronous tasks')


@router.post('/sync', summary='Test adding synchronization task')
async def task_demo_add():
    scheduler.add_job(
        task_demo, 'interval', seconds=1, id='task_demo', replace_existing=True, start_date=datetime.datetime.now()
    )

    return await response_base.success()


@router.post('/async', summary='Test adding an asynchronous task')
async def task_demo_add_async():
    scheduler.add_job(
        task_demo_async,
        'interval',
        seconds=1,
        id='task_demo_async',
        replace_existing=True,
        start_date=datetime.datetime.now(),
    )
    return await response_base.success()


@router.post('/files', summary='Test file upload')
async def create_file(file: bytes = File(), fileb: UploadFile = File(), token: str = Form()):
    return {
        'file_size': len(file),
        'token': token,
        'fileb_content_type': fileb.content_type,
    }
