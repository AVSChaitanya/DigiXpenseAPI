#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Any

from pydantic import BaseModel

from DigiXpenseAPI.app.common.response.response_code import CustomResponseCode
from DigiXpenseAPI.app.core.conf import settings
from DigiXpenseAPI.app.utils.encoders import jsonable_encoder

_ExcludeData = set[int | str] | dict[int | str, Any]

__all__ = ['ResponseModel', 'response_base']


class ResponseModel(BaseModel):
    """
    Unified return model

    .. tip::

        If you don't want to use ResponseBase Custom encoders in can use this model, and the returned data will be automatically parsed and returned through the encoder inside fastapi;
        This return model generates openapi schema documentation

    E.g. ::

        @router.get('/test', response_model=ResponseModel)
        def test():
            return ResponseModel(data={'test': 'test'})

        @router.get('/test')
        def test() -> ResponseModel:
            return ResponseModel(data={'test': 'test'})

        @router.get('/test')
        def test() -> ResponseModel:
            res = CustomResponseCode.HTTP_200
            return ResponseModel(code=res.code, msg=res.msg, data={'test': 'test'})
    """  # noqa: E501

    code: int = CustomResponseCode.HTTP_200.code
    msg: str = CustomResponseCode.HTTP_200.msg
    data: Any | None = None

    class Config:
        json_encoders = {datetime: lambda x: x.strftime(settings.DATETIME_FORMAT)}


class ResponseBase:
    """
    Unified return method

    .. tip::

        The return methods in this class will be pre-parsed by the custom encoder, and then processed and returned again by the encoder inside fastapi. There may be a performance penalty, depending on personal preference;
        This return model does not generate openapi schema documentation

    E.g. ::

        @router.get('/test')
        def test():
            return await response_base.success(data={'test': 'test'})
    """  # noqa: E501

    @staticmethod
    async def __response(
        *, res: CustomResponseCode = None, data: Any | None = None, exclude: _ExcludeData | None = None, **kwargs
    ) -> dict:
        """
        The request returns a common method if successful

        :param code: Return status code
        :param msg: returned messages
        :param data: Return data
        :param exclude: Return data field exclusion
        :param kwargs: jsonable_encoder Configuration items
        :return:
        """
        if data is not None:
            custom_encoder = {datetime: lambda x: x.strftime(settings.DATETIME_FORMAT)}
            kwargs.update({'custom_encoder': custom_encoder})
            data = jsonable_encoder(data, exclude=exclude, **kwargs)
        return {'code': res.code, 'msg': res.msg, 'data': data}

    async def success(
        self,
        *,
        res: CustomResponseCode = CustomResponseCode.HTTP_200,
        data: Any | None = None,
        exclude: _ExcludeData | None = None,
        **kwargs
    ) -> dict:
        return await self.__response(res=res, data=data, exclude=exclude, **kwargs)

    async def fail(
        self,
        *,
        res: CustomResponseCode = CustomResponseCode.HTTP_400,
        data: Any = None,
        exclude: _ExcludeData | None = None,
        **kwargs
    ) -> dict:
        return await self.__response(res=res, data=data, exclude=exclude, **kwargs)


response_base = ResponseBase()
