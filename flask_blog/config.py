class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    # SQLALCHEMY_DATABASE_URI указывает, где и как хранить данные приложения (в данном случае - в файле SQLite)
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    # SECRET_KEY обеспечивает безопасность сессий и других защищённых функций Flask
