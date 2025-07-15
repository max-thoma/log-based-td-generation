from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "@context": ["https://www.w3.org/2019/wot/td/v1"],
            "id": "tv",
            "title": "Vacuum robot",
            "@type": "Vacuum device",
            "description": "A vacuum roboter for cleaning the floor",
            "base": "http://127.0.0.1:5000",
            "owl:sameAs": "test",
            "securityDefinitions": {"basic_sc": {"scheme": "basic", "in": "header"}},
            "security": ["basic_sc"],
            "properties": {
                "cleaning": {
                    "type": "boolean",
                    "title": "Current Cleaning Status",
                    "description": "States if the robot is currently cleaning or not",
                    "forms": [
                        {
                            "mqv:topic": "vacuum/is_cleaning",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "storage_full": {
                    "type": "boolean",
                    "title": "Waste Bin Level",
                    "description": "States whether the storage of the robot is full or not",
                    "forms": [
                        {
                            "mqv:topic": "vacuum/storage_full",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "battery": {
                    "type": "integer",
                    "title": "Battery Level",
                    "description": "Describes the current power charge in percent",
                    "minimum": 0,
                    "maximum": 100,
                    "forms": [
                        {
                            "mqv:topic": "vacuum/battery",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "mapped": {
                    "type": "boolean",
                    "title": "Room Mapping Available",
                    "description": "States whether a current mapping of the room is available, needed in order to start the vacuuming",
                    "forms": [
                        {
                            "mqv:topic": "vacuum/is_mapped",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "at_base": {
                    "type": "boolean",
                    "title": "Robot Base Status",
                    "description": "States whether the robot is currently docked at the charging base station",
                    "forms": [
                        {
                            "mqv:topic": "vacuum/is_at_base",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
            "actions": {
                "start": {
                    "title": "Start Cleaning Cycle",
                    "description": "Starts vacuuming the room, only valid if a mapping for the room and sufficient storage and battery are available",
                    "forms": [
                        {
                            "mqv:topic": "vacuum/start",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "scan": {
                    "title": "Scan Room",
                    "description": "Scans room, creating a mapping",
                    "forms": [
                        {
                            "mqv:topic": "vacuum/scan",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "empty_storage": {
                    "title": "Empty Waste Bin",
                    "description": "Empties storage",
                    "forms": [
                        {
                            "mqv:topic": "vacuum/empty_storage",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "return_to_base": {
                    "title": "Return To Base",
                    "description": "Returns to the base, enables further actions",
                    "forms": [
                        {
                            "mqv:topic": "vacuum/base",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "charge": {
                    "title": "Charge Battery",
                    "description": "Charges robot",
                    "forms": [
                        {
                            "mqv:topic": "vacuum/charge",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
        }
    )
