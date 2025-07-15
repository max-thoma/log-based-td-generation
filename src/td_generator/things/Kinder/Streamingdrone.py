from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "@context": ["https://www.w3.org/2019/wot/td/v1"],
            "id": "streaming_drone",
            "title": "Streaming drone",
            "@type": "Streaming drone",
            "description": "A drone that can be used to stream video",
            "base": "http://127.0.0.1:5000",
            "securityDefinitions": {"basic_sc": {"scheme": "basic", "in": "header"}},
            "security": ["basic_sc"],
            "properties": {
                "recording": {
                    "type": "boolean",
                    "title": "Drone Recording Status",
                    "description": "Indicates if the drone is currently recording or not",
                    "forms": [
                        {
                            "mqv:topic": "streaming_drone/is_recording",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "streaming": {
                    "type": "boolean",
                    "title": "Drone Streaming Status",
                    "description": "Indicates whether the drone is currently live streaming",
                    "forms": [
                        {
                            "mqv:topic": "streaming_drone/is_streaming",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "battery": {
                    "type": "integer",
                    "title": "Drone Battery Level",
                    "description": "Represents the current battery in percentage",
                    "minimum": 0,
                    "maximum": 100,
                    "forms": [
                        {
                            "mqv:topic": "streaming_drone/battery",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
            "actions": {
                "stream": {
                    "title": "Start Streaming",
                    "description": "Starts streaming",
                    "forms": [
                        {
                            "mqv:topic": "streaming_drone/stream",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "stop stream": {
                    "title": "Stop Streaming",
                    "description": "Stops streaming",
                    "forms": [
                        {
                            "mqv:topic": "streaming_drone/stop_stream",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "start recording": {
                    "title": "Start Recording",
                    "description": "Starts the recording",
                    "forms": [
                        {
                            "mqv:topic": "streaming_drone/record",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "end": {
                    "title": "End Recording",
                    "description": "Ends recording process deleting not saved recording",
                    "forms": [
                        {
                            "mqv:topic": "streaming_drone/end",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "recharge": {
                    "title": "Recharge Battery",
                    "description": "Recharges the battery, can not be recharged during streaming or recording",
                    "forms": [
                        {
                            "mqv:topic": "streaming_drone/recharge",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
        }
    )
