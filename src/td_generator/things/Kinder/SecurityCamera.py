from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "@context": ["https://www.w3.org/2019/wot/td/v1"],
            "id": "camera",
            "title": "Security Camera",
            "@type": "Outdoor Video Camera",
            "description": "A security camera that can record video to disk",
            "base": "http://127.0.0.1:5000",
            "owl:sameAs": "test",
            "securityDefinitions": {"basic_sc": {"scheme": "basic", "in": "header"}},
            "security": ["basic_sc"],
            "properties": {
                "recording": {
                    "title": "Recording Status",
                    "type": "boolean",
                    "description": "Boolean value indicating if the camera is currently recording",
                    "forms": [
                        {
                            "mqv:topic": "camera/is_recording",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "storage": {
                    "title": "Recording Storage Disk",
                    "type": "integer",
                    "minimum": 0,
                    "maximum": 256,
                    "description": "States the current remaining storage in gigabytes",
                    "forms": [
                        {
                            "mqv:topic": "camera/storage",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
            "actions": {
                "record": {
                    "title": "Start Recording",
                    "description": "Starts the recording",
                    "forms": [
                        {
                            "mqv:topic": "camera/record/record",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "stop": {
                    "title": "Stop Recording",
                    "description": "Stops the recording",
                    "forms": [
                        {
                            "mqv:topic": "camera/record/stop",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "delete": {
                    "title": "Delete Recording",
                    "description": "Deletes video files freeing storage",
                    "forms": [
                        {
                            "mqv:topic": "camera/record/delete",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
        }
    )
