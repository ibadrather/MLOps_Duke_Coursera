from mlflow import log_metric
from random import choice

metric_names = ["cpu", "ram", "disk"]

percentages = [i for i in range(100)]

for i in range(40):
    log_metric(choice(metric_names), choice(percentages))

# mlflow experiments create --experiment-name produce-metrics

## it will output something like:
## Created experiment 'produce-metrics' with id 246899778805979802

## now we can run the script like this:
# MLFLOW_EXPERIMENT_ID=246899778805979802 python produce-metrics.py
