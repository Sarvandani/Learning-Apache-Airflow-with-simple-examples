#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Sarvandani
"""

from airflow import DAG
from airflow.models.baseoperator import chain
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.mysql.operators.mysql import MySqlOperator
from airflow.hooks.mysql import MySqlHook
from datetime import datetime

# Define a ML function that will be executed as a PythonOperator task
def machine_learning_task(**context):
    # libraries for machine learning
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression

    # Load data and perform machine learning tasks
    data = pd.read_csv('/path/to/data.csv')
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    print("Accuracy:", accuracy)
    
    # Push accuracy as an XCom value
    context['ti'].xcom_push(key='accuracy', value=accuracy)

# Define the DAG
with DAG(
    dag_id="machine_learning_dag",
    description="A DAG for executing a machine learning",
    start_date=datetime(2023, 7, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    # Define the tasks
    task_bash = BashOperator(
        task_id="bash_task",
        bash_command="""
            echo "Executing bash script..."
            # running a python script
            python /path/to/script.py
        """
    )

    task_python = PythonOperator(
        task_id="python_ML",
        python_callable=machine_learning_task,
        provide_context=True  # Passes the context to the Python function
    )

    task_mysql = MySqlOperator(
        task_id="mysql_mytable",
        mysql_conn_id="mysql_default",
        sql="SELECT * FROM my_table"
    )

    # Set task dependencies using Taskflow API
    chain(task_bash, task_python, task_mysql)

    # Retrieve connection using hook
    hook = MySqlHook(mysql_conn_id="mysql_default")

    # Execute a query using hook
    result = hook.get_records("SELECT COUNT(*) FROM my_table")
    print("Number of records:", result[0][0])