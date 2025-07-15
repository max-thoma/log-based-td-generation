from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "@context": ["https://www.w3.org/2019/wot/td/v1"],
            "id": "dryer",
            "title": "Dryer",
            "description": "A laundry dryer appliance",
            "@type": "Dryer",
            "base": "http://127.0.0.1:5000",
            "owl:sameAs": "test",
            "securityDefinitions": {"basic_sc": {"scheme": "basic", "in": "header"}},
            "security": ["basic_sc"],
            "properties": {
                "running": {
                    "type": "boolean",
                    "title": "Dryer Status",
                    "description": "True if the device is currently drying laundry",
                    "forms": [
                        {
                            "mqv:topic": "dryer/running",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "temperature": {
                    "title": "Drying Temperature",
                    "type": "integer",
                    "description": "Displays the current drying temperature, temperature can not be changed during drying process",
                    "minimum": 40,
                    "maximum": 80,
                    "forms": [
                        {
                            "mqv:topic": "dryer/temperature",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "distilled storage": {
                    "title": "Distilled Water Level",
                    "type": "integer",
                    "description": "Displays the current remaining storage for the distilled water output in percentage",
                    "minimum": 0,
                    "maximum": 100,
                    "forms": [
                        {
                            "mqv:topic": "dryer/storage",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
            "actions": {
                "start": {
                    "title": "Start Dryer",
                    "description": "Starts drying process",
                    "forms": [
                        {
                            "mqv:topic": "dryer/start",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "clear": {
                    "title": "Clear Distilled Water",
                    "description": "Clear distilled water storage",
                    "forms": [
                        {
                            "mqv:topic": "dryer/clear",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "increase temperature": {
                    "title": "Increase Temperature",
                    "description": "Increases drying temperature by 10",
                    "forms": [
                        {
                            "mqv:topic": "dryer/increase",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "decrease temperature": {
                    "title": "Decrease Temperature",
                    "description": "Decreases drying temperature by 10",
                    "forms": [
                        {
                            "mqv:topic": "dryer/decrease",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
        }
    )
