import logging
import boto3
import random
import string
from typing import Any, MutableMapping, Optional

from cloudformation_cli_python_lib import (
    Action,
    HandlerErrorCode,
    OperationStatus,
    ProgressEvent,
    Resource,
    SessionProxy,
    exceptions,
)

from .models import ResourceHandlerRequest, ResourceModel

# Use this logger to forward log messages to CloudWatch Logs.
LOG = logging.getLogger(__name__)
TYPE_NAME = "Richard::Resource::Provider"

resource = Resource(TYPE_NAME, ResourceModel)
test_entrypoint = resource.test_entrypoint


@resource.handler(Action.CREATE)
def create_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    model = request.desiredResourceState
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=model,
        callbackContext=callback_context if callback_context is not None else {}
    )
    try:
        if isinstance(session, SessionProxy):
            if "TOKEN" in callback_context and "VERSION" in callback_context:
                response = session.client("cloudformation").set_type_default_version(
                    Arn=callback_context["VERSION"]
                )
                progress.status = OperationStatus.SUCCESS
            elif "TOKEN" in callback_context and "VERSION" not in callback_context:
                response = session.client("cloudformation").describe_type_registration(
                    RegistrationToken=callback_context["TOKEN"]
                )
                if response['ProgressStatus'] == 'COMPLETE':
                    progress.callbackContext["VERSION"] = response["TypeVersionArn"]
                    progress.callbackContext["Arn"] = response["TypeArn"]
                    
                    progress.resourceModel.Version = response["TypeVersionArn"]
                    progress.resourceModel.Arn = response["TypeArn"]
                elif response['ProgressStatus'] == 'FAILED':
                    progress.status = OperationStatus.FAILED
                else:
                    progress.callbackDelaySeconds=30
                    progress.status = OperationStatus.IN_PROGRESS
            else:
                response = session.client("cloudformation").register_type(
                    Type=model.Type if model.Type is not None else 'RESOURCE',
                    TypeName=model.TypeName,
                    SchemaHandlerPackage=model.SchemaHandlerPackage,
                    LoggingConfig={'LogRoleArn': model.LoggingConfig.LogRoleArn, 'LogGroupName': model.LoggingConfig.LogGroupName} if model.LoggingConfig is not None else None,
                    ExecutionRoleArn=model.ExecutionRoleArn if model.ExecutionRoleArn is not None else None,
                    ClientRequestToken=''.join(random.choice(string.ascii_lowercase) for i in range(32))
                )
                progress.callbackContext["TOKEN"] = response["RegistrationToken"]
                progress.resourceModel.Token = response["RegistrationToken"]
                progress.status = OperationStatus.IN_PROGRESS
    except TypeError as e:
        # exceptions module lets CloudFormation know the type of failure that occurred
        raise exceptions.InternalFailure(f"was not expecting type {e}")
        # this can also be done by returning a failed progress event
        # return ProgressEvent.failed(HandlerErrorCode.InternalFailure, f"was not expecting type {e}")
    return progress


@resource.handler(Action.UPDATE)
def update_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    model = request.desiredResourceState
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=model,
    )
    # TODO: put code here
    return progress


@resource.handler(Action.DELETE)
def delete_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    model = request.desiredResourceState
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=model,
    )
    # TODO: put code here
    return progress


@resource.handler(Action.READ)
def read_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    model = request.desiredResourceState
    # TODO: put code here
    return ProgressEvent(
        status=OperationStatus.SUCCESS,
        resourceModel=model,
    )


@resource.handler(Action.LIST)
def list_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    # TODO: put code here
    return ProgressEvent(
        status=OperationStatus.SUCCESS,
        resourceModels=[],
    )
