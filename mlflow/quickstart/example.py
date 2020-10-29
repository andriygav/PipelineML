import os
from random import random, randint

import mlflow
from mlflow import log_metric, log_param, log_artifacts

if __name__ == "__main__":
    mlflow.set_tracking_uri("http://localhost:5000")
    mlflow.set_experiment('example')
    mlflow.start_run()

    log_param("param1", randint(0, 100))

    foo = random()
    log_metric("foo", foo)
    log_metric("foo", random() + 1)
    log_metric("foo", random() + 2)
    
    mlflow.end_run()