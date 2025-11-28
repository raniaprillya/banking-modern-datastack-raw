from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Ganti dengan path direktori yang Anda gunakan
TARGET_BASE_DIR = "/home/popo/banking-modern-datastack"

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 0,  # Matikan retry agar gagal segera terlihat
}

with DAG(
    dag_id="debug_check_base_directory",
    default_args=default_args,
    description="Check existence and permissions of the dbt base directory.",
    schedule_interval=None,
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["debug", "dbt"],
) as dag:

    # 1. Task: Cek Siapa User Airflow
    # Penting untuk tahu siapa yang mencoba mengakses direktori.
    check_user = BashOperator(
        task_id="check_airflow_user",
        bash_command="echo 'Airflow user running this task:' && whoami"
    )

    # 2. Task: Cek Keberadaan dan Izin Direktori Utama
    # Perintah 'ls -ld' akan mencetak detail (izin) direktori jika ada, atau error jika tidak ada.
    check_base_dir_details = BashOperator(
        task_id="check_base_directory_details",
        bash_command=f"echo 'Checking directory details (ls -ld):' && ls -ld {TARGET_BASE_DIR}"
    )

    # 3. Task: Cek Isi Direktori Utama
    # Perintah ini akan gagal jika direktori tidak ada atau user tidak memiliki izin baca/masuk.
    check_base_dir_contents = BashOperator(
        task_id="check_base_directory_contents",
        bash_command=f"echo 'Checking directory contents (ls -l):' && ls -l {TARGET_BASE_DIR}"
    )

    # 4. Task: Cek Keberadaan Sub-Direktori 'banking_dbt'
    check_dbt_project_dir = BashOperator(
        task_id="check_dbt_project_dir",
        bash_command=f"echo 'Checking dbt project directory:' && ls -ld {TARGET_BASE_DIR}/banking_dbt"
    )

    # Definisikan urutan task
    # Cek user -> Cek detail direktori -> Cek isi direktori -> Cek sub-direktori
    check_user >> check_base_dir_details >> check_base_dir_contents >> check_dbt_project_dir