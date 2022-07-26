from ..hexagonalmodel.domain.registry import Registry

def inject(db):
    Registry().stock = db