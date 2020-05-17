# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

from cloudformation_cli_python_lib.interface import (
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class ResourceHandlerRequest(BaseResourceHandlerRequest):
    # pylint: disable=invalid-name
    desiredResourceState: Optional["ResourceModel"]
    previousResourceState: Optional["ResourceModel"]


@dataclass
class ResourceModel(BaseModel):
    Type: Optional[str]
    Arn: Optional[str]
    SetDefault: Optional[bool]
    Version: Optional[str]
    TypeName: Optional[str]
    SchemaHandlerPackage: Optional[str]
    LoggingConfig: Optional["_LoggingConfig"]
    ExecutionRoleArn: Optional[str]
    Token: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Type=json_data.get("Type"),
            Arn=json_data.get("Arn"),
            SetDefault=json_data.get("SetDefault"),
            Version=json_data.get("Version"),
            TypeName=json_data.get("TypeName"),
            SchemaHandlerPackage=json_data.get("SchemaHandlerPackage"),
            LoggingConfig=LoggingConfig._deserialize(json_data.get("LoggingConfig")),
            ExecutionRoleArn=json_data.get("ExecutionRoleArn"),
            Token=json_data.get("Token"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LoggingConfig(BaseModel):
    LogRoleArn: Optional[str]
    LogGroupName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingConfig"]:
        if not json_data:
            return None
        return cls(
            LogRoleArn=json_data.get("LogRoleArn"),
            LogGroupName=json_data.get("LogGroupName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingConfig = LoggingConfig


