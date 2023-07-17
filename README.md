[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)

# Learning-Apache-Airflow-with-simple-examples

<img src="workflow.png">

Apache Airflow is a powerful platform designed for workflow (like photo) and data pipeline management. It enables users to define workflows as directed acyclic graphs (DAGs) and effectively manage their execution. Within Airflow, several key concepts and components contribute to the functionality of DAGs:

1. Scheduling: Scheduling involves determining the timing and execution details of tasks within a DAG. It defines when and how each task should be executed based on specified intervals or triggers.

2. Catchup: Catchup is a parameter that determines whether Airflow should create DAG runs for all schedule intervals from the start date until the current date (catchup=True) or schedule runs only from the current date (catchup=False).

3. Backfilling: Backfilling extends the capabilities of scheduling by enabling the creation of past runs from the command-line interface (CLI), regardless of the catchup parameter’s value.

A simple code of DAG can be seen [here](https://github.com/Sarvandani/Learning-Apache-Airflow-with-simple-examples/blob/main/dag.py). 

4. Task: Each task within a DAG represents a distinct unit of work that needs to be executed. Tasks can be executed independently or in a specific order, depending on their defined dependencies.

5. Operator: Operators are used to define tasks within a DAG. Examples of operators include BashOperator, PythonOperator, and MySqlOperator. These operators encapsulate the logic and functionality of the tasks they represent. Now we have added the task, operator and task dependency to the code. You can download it [here](https://github.com/Sarvandani/Learning-Apache-Airflow-with-simple-examples/blob/main/task%2Boperators.py).

6. Task Dependency: Task dependencies define the relationship between tasks within a DAG. They specify the order in which tasks should be executed and are typically defined using the >> symbol. Task dependencies can also be defined using the set_downstream() and set_upstream() methods. 

7. XComs: XComs facilitate communication and data exchange between tasks within a DAG. They allow tasks to share data, such as variables or results, by pushing and pulling values between tasks. We can see in the following code, how XComs works in Airflow. Download the code [here](https://github.com/Sarvandani/Learning-Apache-Airflow-with-simple-examples/blob/main/XCOM.py).

8. Connections: Connections in Airflow represent the configuration details required to connect to external systems or services. They store information such as database credentials, API keys, and connection URLs.

9. Hooks: Hooks provide an interface to interact with specific types of external systems or services. They abstract the interaction details, enabling tasks to easily connect and communicate with external resources through predefined methods and functionality. The changes of the code after adding Hook is written now. The code is available [here](https://github.com/Sarvandani/Learning-Apache-Airflow-with-simple-examples/blob/main/hook.py).

10. Taskflow: Taskflow API is a higher-level abstraction in Airflow that offers advanced features and flexibility for defining complex workflows and dependencies. It provides a more intuitive way to structure and manage workflows, utilizing the power of DAGs and operators. Updated code is [here](https://github.com/Sarvandani/Learning-Apache-Airflow-with-simple-examples/blob/main/taskflow.py).
