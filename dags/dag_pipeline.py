from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'epsi_data_team',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id='sales_pipeline_dag',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    description='Pipeline DataOps de ventes avec dbt & GE',
    tags=['sales', 'dataops', 'dbt', 'great_expectations'],
) as dag:

    ingest_data = BashOperator(
        task_id='ingest_sales_data',
        bash_command='echo "Ingestion simulée : fichier sales.csv déjà disponible dans /data."'
    )

    run_dbt_models = BashOperator(
        task_id='run_dbt_models',
        bash_command='cd /workspace/dbt && dbt run'
    )

    run_data_tests = BashOperator(
        task_id='run_great_expectations_tests',
        bash_command='great_expectations checkpoint run sales_checkpoint'
    )

    notify_success = BashOperator(
        task_id='notify_success',
        bash_command='echo "Pipeline exécuté avec succès !"'
    )

    ingest_data >> run_dbt_models >> run_data_tests >> notify_success
