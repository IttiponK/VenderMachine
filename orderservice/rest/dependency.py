from ..hexagonalmodel.domain.registry import Registry
from ..hexagonalmodel.adapter.mysqlinsqlalchemy import MySQLinSQLAlchemy
from ..infrastructure.mysql.connect import connect_mysql_db
from nameko.standalone.rpc import ClusterRpcProxy

def inject():
    connect,transaction = connect_mysql_db()
    Registry().transaction = MySQLinSQLAlchemy(connect=connect,transaction=transaction)
    broker_cfg = {'AMQP_URI': "amqp://guest:guest@rabbitmq"}
    Registry().rpc = ClusterRpcProxy(broker_cfg)