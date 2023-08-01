from settings import Base, engine, app
from views import router


def create_tables():
    Base.metadata.create_all(bind = engine)
    
    
app.include_router(router)
create_tables()

#Запусти сначала сам  файл