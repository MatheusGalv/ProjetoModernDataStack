from time import sleep

from airflow.decorators import dag, task

from datetime import datetime

@dag(
        dag_id="ModernDataStack",
        description="Minha ETL Braba",
        schedule="* * * * *",
        start_date=datetime(2024, 5, 24),
        catchup=False
)
def pipeline():

    @task
    def primeira_atividade():
        print("primeira atividade rodou com sucesso")
        sleep(2)

    @task
    def segunda_atividade():
        print("Segunda atividade rodou com sucesso")
        sleep(2)

    @task
    def terceira_atividade():
        print("terceira atividade rodou com sucesso")
        sleep(2)


    t1 = primeira_atividade()
    t2 = segunda_atividade()
    t3 = terceira_atividade()

pipeline()

