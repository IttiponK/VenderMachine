from .initapp import create_app 
from ..hexagonalmodel.domain.model.stock import Stock
from ..hexagonalmodel.adapter.mysqlinsqlalchemy import MySQLinSQLAlchemy


app = create_app(MySQLinSQLAlchemy(Stock))