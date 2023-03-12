# coding: utf-8

"""
    DJ server

    A DataJunction metrics layer  # noqa: E501

    The version of the OpenAPI document: 0.0.post1.dev1+g5d0aa56
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from djclient import schemas  # noqa: F401


class AttributeOutput(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Column attribute output.
    """


    class MetaOapg:
        required = {
            "attribute_type",
        }
        
        class properties:
        
            @staticmethod
            def attribute_type() -> typing.Type['AttributeTypeName']:
                return AttributeTypeName
            __annotations__ = {
                "attribute_type": attribute_type,
            }
    
    attribute_type: 'AttributeTypeName'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attribute_type"]) -> 'AttributeTypeName': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["attribute_type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attribute_type"]) -> 'AttributeTypeName': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["attribute_type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        attribute_type: 'AttributeTypeName',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AttributeOutput':
        return super().__new__(
            cls,
            *_args,
            attribute_type=attribute_type,
            _configuration=_configuration,
            **kwargs,
        )

from djclient.model.attribute_type_name import AttributeTypeName
