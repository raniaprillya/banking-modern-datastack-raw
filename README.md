# Modern Data Stack Pipeline (Docker + Airflow + DBT + PostgreSQL + Kafka + Debezium + Snowflake)

## 📌 Overview

Project ini merupakan implementasi **modern data pipeline end-to-end** menggunakan konsep **ELT**, **Change Data Capture (CDC)**, dan **workflow orchestration**.

Draft ini mengikuti arsitektur dan langkah-langkah pada video:
🔗 [https://www.youtube.com/watch?v=uHiyZitmIS0](https://www.youtube.com/watch?v=uHiyZitmIS0)

Dalam pipeline ini:

* **Raw data di-*generate*** menggunakan Python fake data generator.
* Data tersebut disimpan ke **PostgreSQL** sebagai source system.
* Setiap perubahan data ditangkap oleh **Debezium** melalui mekanisme **CDC** dan dikirimkan ke **Kafka** sebagai event stream.
* **Airflow** bertindak sebagai orchestrator untuk melakukan proses extract → load → trigger transformasi.
* **DBT** menjalankan transformasi di Snowflake menggunakan pendekatan **Slowly Changing Dimension (SCD) Type 2**.
* Hasil akhir disimpan di **Snowflake** sebagai data warehouse untuk analitik.
