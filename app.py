from flask import Flask
import uvicorn
from fastapi import FastAPI
from BankNotes import BankNote
import numpy as np
import pickle
import pandas as pd

app = Flask(__name__)

@app.get('/{name}')
@app.get('/')
def get_name(name: str = None):
    if name:
        return {'Welcome': f'{name}'}
    else:
        return {'message': 'Hello, 9999!'}


if __name__ == '__main__':
    app.run()