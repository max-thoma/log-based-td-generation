from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "@context": ["https://www.w3.org/2019/wot/td/v1"],
            "id": "stove",
            "title": "Stove",
            "@type": "Kitchen device",
            "description": "A two plate electric stove",
            "base": "http://127.0.0.1:5000",
            "owl:sameAs": "test",
            "securityDefinitions": {"basic_sc": {"scheme": "basic", "in": "header"}},
            "security": ["basic_sc"],
            "properties": {
                "plate_1_power": {
                    "title": "Plate 1 Power Status",
                    "type": "boolean",
                    "description": "Indicates whether plate 1 is currently turned on or off",
                    "forms": [
                        {
                            "mqv:topic": "stove/plate_1_power",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "plate_2_power": {
                    "title": "Plate 2 Power Status",
                    "type": "boolean",
                    "description": "Indicates whether plate 2 is currently turned on or off",
                    "forms": [
                        {
                            "mqv:topic": "stove/plate_2_power",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "plate_1_level": {
                    "title": "Plate 1 Power Level",
                    "type": "integer",
                    "description": "Represents the current heating level of plate 1",
                    "minimum": 0,
                    "maximum": 9,
                    "forms": [
                        {
                            "mqv:topic": "stove/plate_1_level",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "plate_2_level": {
                    "type": "integer",
                    "title": "Plate 2 Power Level",
                    "description": "Represents the current heating level of plate 2",
                    "minimum": 0,
                    "maximum": 9,
                    "forms": [
                        {
                            "mqv:topic": "stove/plate_2_level",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
            "actions": {
                "activate_plate_1": {
                    "title": "Activate Plate 1",
                    "description": "Activates plate 1 setting its power level to True",
                    "forms": [
                        {
                            "mqv:topic": "stove/activate_plate_1",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "activate_plate_2": {
                    "title": "Activate Plate 2",
                    "description": "Activates plate 2 setting its power level to True",
                    "forms": [
                        {
                            "mqv:topic": "stove/activate_plate_2",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "deactivate_plate_1": {
                    "title": "Deactivate Plate 1",
                    "description": "Deactivates plate 1 setting its power level to False",
                    "forms": [
                        {
                            "mqv:topic": "stove/deactivate_plate_1",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "deactivate_plate_2": {
                    "title": "Deactivate Plate 2",
                    "description": "Deactivates plate 2 setting its power level to False",
                    "forms": [
                        {
                            "mqv:topic": "stove/deactivate_plate_2",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "increase_heat_plate_1": {
                    "title": "Increase Heat Plate 1",
                    "description": "Increases the heating level for plate 1 by 1",
                    "forms": [
                        {
                            "mqv:topic": "stove/increase_heat_plate_1",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "increase_heat_plate_2": {
                    "title": "Increase Heat Plate 2",
                    "description": "Increases the heating level for plate 2 by 1",
                    "forms": [
                        {
                            "mqv:topic": "stove/increase_heat_plate_2",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "decrease_heat_plate_1": {
                    "title": "Decrease Heat Plate 1",
                    "description": "Increases the heating level for plate 1 by 1",
                    "forms": [
                        {
                            "mqv:topic": "stove/decrease_heat_plate_1",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "decrease_heat_plate_2": {
                    "title": "Decrease Heat Plate 2",
                    "description": "Increases the heating level for plate 2 by 1",
                    "forms": [
                        {
                            "mqv:topic": "stove/decrease_heat_plate_2",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
        }
    )
