import os
import pickle
import argparse

import mlflow
from mlflow import log_metric, log_param, log_artifacts

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--experiment', default = 'linear', help='experiment ir')
    parser.add_argument('--server', default = 'http://localhost:5000', help='server host')
    parser.add_argument('--C', type=float, default = 1.0, help='inverse of regularization strength')
    parser.add_argument('--penalty', default = 'l2', choices=['l1','l2'], help='the norm used in the penalization')
    namespace = parser.parse_args()
    argv = vars(namespace)
    
    mlflow.set_tracking_uri(argv['server'])
    mlflow.set_experiment(argv['experiment'])
    mlflow.start_run()
    
    X, Y = make_classification(n_samples=400, n_features=2, 
                               n_informative=2, n_classes=2, 
                               n_redundant=0,
                               n_clusters_per_class=1,
                               random_state=0)
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=100, random_state=0)
   
    log_param("C", argv['C'])
    log_param("penalty", argv['penalty'])
    
    model = LogisticRegression(C=argv['C'], penalty=argv['penalty'], solver='saga')
    
    model.fit(X_train, Y_train)
    
    log_metric("train acc", model.score(X_train, Y_train))
    log_metric("test acc", model.score(X_test, Y_test))
    
    mlflow.end_run()