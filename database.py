from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json,os

#with open('/mnt/secrets-store/arn:aws:secretsmanager:ap-northeast-2:865577889736:secret:dev_rds-rftU0T', 'r') as secret_file:
#    secret_data = json.load(secret_file)

#DB_USERNAME = secret_data['username']
#DB_PASSWORD = secret_data['password']
#DB_HOST = secret_data['host']
#DB_PORT = secret_data['port']
#DB_NAME = secret_data['dbname']


# SQLAlchemy 엔진 생성
DATABASE_URL = f"mysql+pymysql://user:1234@10.104.121.231:3306/db"

os.environ['DATABASE_URL'] = DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
