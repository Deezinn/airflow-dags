"""
segunda DAG v0: Hello world
"""

from datetime import datetime

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.empty import EmptyOperator

minha_dag = DAG(
    dag_id="a_segunda_dag_v0",
    start_date=datetime(2025, 8, 13),
    schedule="@daily",
    catchup=False,
    doc_md=__doc__,
)

start = EmptyOperator(task_id="start", dag=minha_dag)
hello = BashOperator(
    task_id="hello", bash_command='echo "Hi from bash operator"', dag=minha_dag
)
end = EmptyOperator(task_id="end", dag=minha_dag)

start >> hello >> end
