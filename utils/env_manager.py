# utils/env_manager.py
import os
import json

def get_env_var(name, default=None):
    return os.getenv(name, default)

def load_env_config(env="dev"):
    with open("config/environment_config.json") as f:
        config = json.load(f)
    return config.get(env, {})
