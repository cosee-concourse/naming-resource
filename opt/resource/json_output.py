import json
import model
import name_generator


def check_output(versions):
    if versions is None:
        return json.dumps([])
    else:
        version_dictionary = []
        for version in versions:
            version_dictionary.append({model.VERSION_JSON_NAME: version})
        return json.dumps(version_dictionary)


def inout_output(version, prefix):
    return json.dumps({"heroku": name_generator.generate_heroku(version, prefix),
                       "default": name_generator.generate_default(version, prefix)}, sort_keys = True)