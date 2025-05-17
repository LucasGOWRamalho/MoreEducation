#!/usr/bin/env python3
"""
Script para inicialização do banco de dados
"""
import os
import sys
from sqlalchemy import create_engine

# Adicione o caminho do projeto ao PYTHONPATH (CORREÇÃO AQUI)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.config import settings
from app.models.base import Base  # Importe seus modelos

def init_db():
    try:
        engine = create_engine(settings.DATABASE_URL)
        
        if settings.DATABASE_URL.startswith("sqlite"):
            from sqlalchemy.engine import Engine
            from sqlalchemy import event
            
            @event.listens_for(Engine, "connect")
            def set_sqlite_pragma(dbapi_connection, connection_record):
                cursor = dbapi_connection.cursor()
                cursor.execute("PRAGMA foreign_keys=ON")
                cursor.close()
        
        Base.metadata.create_all(bind=engine)
        print(f"✅ Banco criado com sucesso em: {settings.DATABASE_URL}")
        print(f"✅ Tabelas criadas: {Base.metadata.tables.keys()}")
    except Exception as e:
        print(f"❌ Erro ao criar banco: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    init_db()

# Linha em branco final (importante)