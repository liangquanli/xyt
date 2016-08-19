#!/usr/bin/env python
# encoding: utf-8


def import_global_module(module, current_locals, current_globals, exceptions=None):
    """Import the requested module into the global scope
    Warning! This will import your module into the global scope

    **Example**:
        from django.conf import settings
        import_global_module(settings, locals(), globals())

    :param module: the module which to import into global scope
    :param current_locals: the local globals
    :param current_globals: the current globals
    :param exceptions: the exceptions which to ignore while importing

    """
    try:
        try:
            objects = getattr(module, '__all__', dir(module))

            for k in objects:
                if k and k[0] != '_':
                    current_globals[k] = getattr(module, k)
        except exceptions, e:
            return e
    finally:
        del current_globals, current_locals


def init_from_object(config):
    import_global_module(config, locals(), globals())


def import_by_name(name):
    """
    基于类名称引用类
    """
    name = str(name)
    tmp = name.split(".")
    module_name = ".".join(tmp[0:-1])
    obj_name = tmp[-1]
    module = __import__(module_name, globals(), locals(), [str(obj_name)])
    return getattr(module, obj_name)


def import_module_by_path(path):
    name = str(path)
    tmp = name.split(".")
    module_name = ".".join(tmp[0:-1])
    obj_name = tmp[-1]
    module = __import__(path, globals(), locals(), [str(obj_name)])
    return module


def import_from_path(path):
    module = import_module_by_path(path)
    init_from_object(module)