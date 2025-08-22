#Ha 6 formas de config deste ficheiros __init__.py:

x=1

if x==1:    
    # 1. PackT/__init__.py
    from .ModuleZ import funcX, constY


else:

    # 2. PackT/__init__.py
    from .ModuleZ import funcX, constY

    __all__ = ["funcX", "constY"]



    # 3.PackT/__init__.py
    from . import ModuleZ

    funcX = ModuleZ.funcX
    constY = ModuleZ.constY




    # 4. PackT/__init__.py
    from . import ModuleZ

    globals().update({
        "funcX": ModuleZ.funcX,
        "constY": ModuleZ.constY
    })




    # 5. PackT/__init__.py
    import importlib

    ModuleZ = importlib.import_module(".ModuleZ", package=__name__)
    funcX = ModuleZ.funcX
    constY = ModuleZ.constY


    # 6. PackT/__init__.py
    from . import ModuleZ

    def __getattr__(name):
        if name in ("funcX", "constY"):
            return getattr(ModuleZ, name)
        raise AttributeError(f"module {__name__} has no attribute {name}")
