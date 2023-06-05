from mlflow import log_metric, log_param, log_artifact
import mlflow


if __name__ == "__main__":
    with mlflow.start_run():
        log_param("threshold", 0.75)
        log_param("verbosity", "DEBUG")

        log_metric("timestamp", 100000)
        log_metric("TTC", 33)

        log_artifact(local_path="4_MLflow_and_Hugging_Face/week1_mlflow/1_using_mlflow/producded-dataset.csv")