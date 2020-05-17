# Richard::Resource::Provider

An example resource schema demonstrating some basic constructs and validation rules.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Richard::Resource::Provider",
    "Properties" : {
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#setdefault" title="SetDefault">SetDefault</a>" : <i>Boolean</i>,
        "<a href="#typename" title="TypeName">TypeName</a>" : <i>String</i>,
        "<a href="#schemahandlerpackage" title="SchemaHandlerPackage">SchemaHandlerPackage</a>" : <i>String</i>,
        "<a href="#loggingconfig" title="LoggingConfig">LoggingConfig</a>" : <i><a href="loggingconfig.md">LoggingConfig</a></i>,
        "<a href="#executionrolearn" title="ExecutionRoleArn">ExecutionRoleArn</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Richard::Resource::Provider
Properties:
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#setdefault" title="SetDefault">SetDefault</a>: <i>Boolean</i>
    <a href="#typename" title="TypeName">TypeName</a>: <i>String</i>
    <a href="#schemahandlerpackage" title="SchemaHandlerPackage">SchemaHandlerPackage</a>: <i>String</i>
    <a href="#loggingconfig" title="LoggingConfig">LoggingConfig</a>: <i><a href="loggingconfig.md">LoggingConfig</a></i>
    <a href="#executionrolearn" title="ExecutionRoleArn">ExecutionRoleArn</a>: <i>String</i>
</pre>

## Properties

#### Type

The kind of type.

Currently, the only valid value is RESOURCE.

Possible values:

RESOURCE

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetDefault

Set this as the default version after registering

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TypeName

The name of the type being registered.

We  recommend  that type names adhere to the following pattern: com-pany_or_organization ::service ::type .

_Required_: Yes

_Type_: String

_Pattern_: <code>^[A-Za-z]+::[A-Za-z]+::[A-Za-z]+$</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SchemaHandlerPackage

A url to the S3 bucket containing the schema handler package that contains the schema, event handlers, and associated  files  for  the type you want to register.

For  information on generating a schema handler package for the type you want to register, see submit  in  the  CloudFormation  CLI  User Guide .

_Required_: Yes

_Type_: String

_Pattern_: <code>^S3:\/\/[a-zA-Z0-9][a-zA-Z0-9\.-]{0,61}[a-zA-Z0-9]$</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingConfig

_Required_: No

_Type_: <a href="loggingconfig.md">LoggingConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExecutionRoleArn

The  Amazon  Resource Name (ARN) of the IAM execution role to use to register the type. If your resource type calls AWS APIs  in  any  of its  handlers,  you  must  create  an  *  IAM  execution role * that includes the necessary permissions to call those AWS APIs, and  pro- vision  that  execution  role  in  your account. CloudFormation then assumes that execution role to provide your resource type  with  the appropriate credentials.

_Required_: No

_Type_: String

_Pattern_: <code>arn:aws:iam::\d{12}:role/?[a-zA-Z_0-9+=,\.@\-_/]+</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Token.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### Version

Active Version for this registration

#### Arn

Arn for registered type version

#### Token

Registration Token for Type Version

