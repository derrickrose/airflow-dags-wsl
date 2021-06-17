from airflow import DAG
from datetime import datetime, timedelta
from operators import ReviewOperator

default_arguments = {
    'owner': "frils",
    'start_date': datetime(2021, 5, 21, 0, 0, 0),
    'retries': 3,
    'retry_delay': timedelta(minutes=10)
}

dag = DAG(
    dag_id="review_dag_test",
    max_active_runs=5,
    schedule_interval='@hourly',
    default_args=default_arguments,
    catchup=False
)

""""""
review_operator = ReviewOperator(
    task_id="review_operator",
    param="some random text",
    dag=dag)

review_operator = ReviewOperator(
    task_id="review_operator",
    param="some random text",
    dag=dag)

review_operator >> review_operator
""""""
