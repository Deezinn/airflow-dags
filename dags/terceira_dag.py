"""
terceira DAG v0: Hello world
"""

from datetime import datetime

from airflow.decorators import dag
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.empty import EmptyOperator


@dag(
    dag_id="a_terceira_dag_v0",
    start_date=datetime(2025, 8, 13),
    schedule="@daily",
    catchup=False,
    doc_md=__doc__,
)
def a_terceira_dag():
    start = EmptyOperator(task_id="start")
    hello = BashOperator(task_id="hello", bash_command='echo "Hi from bash operator"')
    end = EmptyOperator(task_id="end")
    start >> hello >> end


criar_dag = a_terceira_dag()
