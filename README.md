# PostgreSQL API

## 📄 Description  
This project provides a Flask-based API for internal PostgreSQL data access. It establishes connections to a PostgreSQL database and executes SQL queries to retrieve and structure.
This API is intended exclusively for internal use within a secure infrastructure. It is deployed on a remote Linux server and used as part of Airflow-managed data pipelines, streamlining interactions between ETL workflows and PostgreSQL databases eliminating the need to import PostgreSQL interaction modules in each pipeline.

## Notes
- Credentials and access are restricted to internal systems and trusted services;
- In trusted indoor environments, it is possible to adapt the system to hold fixed credentials;
- Used to simplify data acquisition within automated data pipelines;

## Features  
- Connects to a PostgreSQL database using user-supplied credentials;
- Fetches all data based on SQL querys and returns it in JSON format;
- Basic data type handling for JSON compatibility;

## Endpoints
```
GET /query/<user>/<password>/<host>/<dbname>/<query>
```
Fetches and returns data based on a SQL query.
Example:
```
GET /query/myuser/mypassword/dbhost/dbname/SELECT * FROM table_x LIMIT 5
```

## 🗂️ Project Structure  
```
project-root/
│
├── src/
│   ├── api/                # API route definitions
│   ├── db/                 # DB connection and queries
│   ├── services/           # Data formatting logic
│   └── main.py             # Application entry point
│
├── requirements.txt      
└── README.md
```

## Running the API

1. Clone the repository:  
```bash
git clone https://github.com/Jose-Nt/api-postgresql.git
cd api-postgresql
```

2. Install dependencies:  
```bash
pip install -r requirements.txt
```

3. Start the API:  
```bash
python src/main.py
```

## 👤 Authors
- José Neto Souza (Jose-Nt)

## License
Free use permitted — attribution required.
