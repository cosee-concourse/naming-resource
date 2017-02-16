checkSchema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "source": {
            "type": "object",
            "properties": {
                "prefix": {
                    "type": "string"
                },

            },
            "required": [
                "prefix"
            ]
        },
        "version": {
            "type": "object",
            "properties": {
                "version": {
                    "type": "string"
                }
            },
            "required": [
                "version"
            ]
        }
    },
    "required": [
        "source"
    ]
}

outSchema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "source": {
            "type": "object",
            "properties": {
                "prefix": {
                    "type": "string"
                },

            },
            "required": [
                "prefix"
            ]
        },
        "names": {
            "type": "object",
            "properties": {
                "default": {
                    "type": "string"
                },
                "heroku": {
                    "type": "string"
                }
            },
            "required": [
                "default",
                "heroku"
            ]
        }
    },
    "required": [
        "source",
        "names"
    ]
}