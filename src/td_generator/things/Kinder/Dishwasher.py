from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "@context": ["https://www.w3.org/2019/wot/td/v1"],
            "id": "dishwasher",
            "title": "Dishwasher",
            "description": "A dishwasher with remote control and monitoring capabilities",
            "@type": "Smart Connected Dishwasher",
            "base": "http://127.0.0.1:5000",
            "owl:sameAs": "test",
            "securityDefinitions": {"basic_sc": {"scheme": "basic", "in": "header"}},
            "security": ["basic_sc"],
            "properties": {
                "running": {
                    "type": "boolean",
                    "title": "Dishwasher Status",
                    "description": "States whether the dishwasher is currently running and washing dishes or not",
                    "forms": [
                        {
                            "mqv:topic": "dishwasher/is_running",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "door": {
                    "type": "string",
                    "title": "Door Position",
                    "description": "Represents if the dishwasher is currently closed or open",
                    "characteristics": ["open", "closed"],
                    "enum": ["open", "closed"],
                    "forms": [
                        {
                            "mqv:topic": "dishwasher",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
            "actions": {
                "close": {
                    "title": "Close Door",
                    "description": "Closes the door",
                    "forms": [
                        {
                            "mqv:topic": "dishwasher/close",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "open": {
                    "title": "Open Door",
                    "description": "Opens the door",
                    "forms": [
                        {
                            "mqv:topic": "dishwasher/open",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "stop": {
                    "title": "Stop Dishwasher",
                    "description": "Stops the washing process",
                    "forms": [
                        {
                            "mqv:topic": "dishwasher/stop",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "start": {
                    "title": "Start Dishwasher",
                    "description": "Starts the washing process",
                    "forms": [
                        {
                            "mqv:topic": "dishwasher/break",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
        }
    )
