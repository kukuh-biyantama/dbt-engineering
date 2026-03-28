from dotenv import load_dotenv
import os
load_dotenv()

db_configlocal = {
    "host": os.getenv("DB_HOST_LOCAL"),
    "port": int(os.getenv("DB_PORT_LOCAL", 5432)),
    "user": os.getenv("DB_USER_LOCAL"),
    "password": os.getenv("DB_PASSWORD_LOCAL"),
    "dbname": os.getenv("DB_NAME_LOCAL"),
}     

db_configkemendagri = {
    "host": os.getenv("DB_HOST_KEMENDAGRI"),    
    "port": int(os.getenv("DB_PORT_KEMENDAGRI", 5432)),
    "user": os.getenv("DB_USER_KEMENDAGRI"),
    "password": os.getenv("DB_PASSWORD_KEMENDAGRI"),
    "dbname": os.getenv("DB_NAME_KEMENDAGRI"),
}