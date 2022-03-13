from airflow import DAG
from airflow.decorators import task
from datetime import datetime

with DAG(dag_id="get_price_FB",
         start_date=datetime(2021, 1, 1),
         schedule_interval="@weekly",
         catchup=False) as dag:
    @task
    def extract(symbol):
        return symbol


    @task
    def process(symbol):
        return symbol


    @task
    def store(symbol):
        return symbol


    store(process(extract(198)))