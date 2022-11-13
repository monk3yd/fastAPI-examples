#!/bin/bash

# uvicorn <file_name_without_ext>:<fastapi_instance_name>
# --reload : reload server when changes detected
uvicorn worker:app --reload