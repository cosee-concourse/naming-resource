def generate_default(version, prefix):
    default = prefix + "." + version
    default = default.replace(".", "_")
    default = default.replace("-", "_")
    return default


def generate_heroku(version, prefix):
    default = prefix + "." + version
    default = default.replace(".", "-")
    return default