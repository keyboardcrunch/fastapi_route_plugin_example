""" Example plugin framework for extending FastAPI routes automagically. """
import importlib
import pkgutil
import sys
from fastapi import FastAPI
import plugins

app = FastAPI()

def import_submodules(module):
    """Import all submodules of a module, recursively."""
    for loader, module_name, is_pkg in pkgutil.walk_packages(
            module.__path__, module.__name__ + '.'):
        importlib.import_module(module_name)
        try:
            app.include_router(getattr(sys.modules[module_name], 'router'))
        except Exception as err:
            print(module_name + " : " + err)
            continue

import_submodules(plugins)

@app.get("/")
async def index():
    """ landing page """
    return [{"result": "index"}]
