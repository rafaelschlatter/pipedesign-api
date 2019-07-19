import os
from src import create_app


ENV = os.environ["ENV"] if "ENV" in os.environ else "dev"

# For Azure app service
app = create_app(config_name=ENV)

# For easy local testing
if __name__ == '__main__':
    local_app = create_app(config_name=ENV)
    local_app.run()
