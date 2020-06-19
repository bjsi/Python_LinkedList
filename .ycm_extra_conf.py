import os


root = os.path.dirname(__file__)


def Settings(**kwargs):
    return {
            'interpreter_path': os.path.join(root, 'env/bin/python3')
            }
