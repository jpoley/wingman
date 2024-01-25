from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def transform_task_1(**context):
    # Get the value from the previous step using XCom
    value = context['ti'].xcom_pull(task_ids='start_task')
    
    # Perform transform
    transformed_value = value * 2
    
    # Log the transform
    print(f"Transformed value at task 1: {transformed_value}")
    
    # Pass the transformed value to the next step using XCom
    context['ti'].xcom_push(key='transformed_value', value=transformed_value)

def transform_task_2(**context):
    # Get the value from the previous step using XCom
    value = context['ti'].xcom_pull(task_ids='task_1')
    
    # Perform transform
    transformed_value = value + 5
    
    # Log the transform
    print(f"Transformed value at task 2: {transformed_value}")
    
    # Pass the transformed value to the next step using XCom
    context['ti'].xcom_push(key='transformed_value', value=transformed_value)

def transform_task_3(**context):
    # Get the value from the previous step using XCom
    value = context['ti'].xcom_pull(task_ids='task_2')
    
    # Perform transform
    transformed_value = value - 10
    
    # Log the transform
    print(f"Transformed value at task 3: {transformed_value}")
    
    # Pass the transformed value to the next step using XCom
    context['ti'].xcom_push(key='transformed_value', value=transformed_value)

# Define the DAG
dag = DAG(
    'xcom_transform_dag',
    description='DAG with XCom transforms',
    schedule_interval=None,
    start_date=datetime(2022, 1, 1),
    catchup=False
)

# Define the tasks
start_task = PythonOperator(
    task_id='start_task',
    python_callable=lambda: 10,  # Initial value
    dag=dag
)

task_1 = PythonOperator(
    task_id='task_1',
    python_callable=transform_task_1,
    provide_context=True,
    dag=dag
)

task_2 = PythonOperator(
    task_id='task_2',
    python_callable=transform_task_2,
    provide_context=True,
    dag=dag
)

task_3 = PythonOperator(
    task_id='task_3',
    python_callable=transform_task_3,
    provide_context=True,
    dag=dag
)

# Define the task dependencies
start_task >> task_1 >> task_2 >> task_3
