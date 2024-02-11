#!/usr/bin/python3
"""__init__ magic method for models directory"""
from models.engine.file_storage import FileStorage

# singleton instance creation of FileStorage
storage = FileStorage()
storage.reload()

def get_storage():
    return storage

