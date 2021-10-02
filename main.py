from fastapi import FastAPI
import importlib
import pkgutil
import plugins
import sys

app = FastAPI()

def import_submodules(module):
    """Import all submodules of a module, recursively."""
    for loader, module_name, is_pkg in pkgutil.walk_packages(
            module.__path__, module.__name__ + '.'):
        importlib.import_module(module_name)
        try:
            app.include_router(getattr(sys.modules[module_name], 'router'))
        except:
            print("Failed to add route from " + module_name)
            continue

import_submodules(plugins)

@app.get("/")
async def index():
    return [{"result": "index"}]