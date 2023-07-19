# all the following deps are referenced directly from the python sdk
import json
from typing import Dict
from message import Message


def lambda_handler(event, context):

    #headers we use to send back data to the caller
    headers: Dict[str, str] = {
        "Content-Type": "application/json",
        "X-Custom-Header": "application/json"
    }

    try:
        #attempt to parse the json into Message by passing in a dictionary
        message = json.loads(event["body"], object_hook=lambda d: Message(**d))
    except json.JSONDecodeError as e:
        return {
            "body": json.dumps({str(e)}),
            "headers": headers,
            "statusCode": 400
        }

    # info on how to use the context object https://docs.aws.amazon.com/lambda/latest/dg/python-context.html
    # convert the message object back into a json
    json_object = {
        "context-arn": str(context.invoked_function_arn),
        "event": str(event),
        "event-body": str(event["body"]),  # the event-body is effectively the message

        #we parse the event-body (aka message) above
        "message-subject": message.subject,
        "message-body": message.body,
        "message-email": message.email
    }

    #send to SES code


    # and return it
    return {
        "body": json.dumps(json_object),
        "headers": headers,
        "statusCode": 201
    }

