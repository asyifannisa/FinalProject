from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns=None):
        self.columns = list(columns) if columns is not None else []
    def fit(self, X, y=None): return self
    def transform(self, X): return X.drop(self.columns, axis=1, errors="ignore")