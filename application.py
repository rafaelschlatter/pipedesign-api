import os, sys
from ml_api.server import server


# Need to import all resources and models to register with the server
from ml_api.resources.machine_learning import *
from ml_api.resources.ml_model import *
from ml_api.resources.pipedesign import * 

from ml_api.models.pipedesign_model import *
from ml_api.models.ml_model_model import *

if __name__ == '__main__':
    server.run()
