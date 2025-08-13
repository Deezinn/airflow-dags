"""
Primeira DAG v0: Hello world
"""

from airflow import DAG
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="a_primeira_dag_v0",
    start_date=datetime(2025, 8, 13),
    schedule="@daily",
    catchup=False,
    doc_md=__doc__,
) as dag:

    start = EmptyOperator(task_id="start")

    hello = BashOperator(
        task_id="hello",
        bash_command='echo "Hi from bash operator"',
    )

    end = EmptyOperator(task_id="end")

    start >> hello >> end
