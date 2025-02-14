from flask import Flask
import psycopg2

app = Flask(__name__)

def connect_db():
    try:
        conn = psycopg2.connect(
            dbname="mydatabase",
            user="postgres",
            password="password",
            host="postgres_db",
            port="5432"
        )
        return conn
    except Exception as e:
        return str(e)

@app.route('/')
def home():
    conn = connect_db()
    if isinstance(conn, str):
        return f"Database connection failed: {conn}"
    return "Successfully developed and deployed multi-container application !"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
