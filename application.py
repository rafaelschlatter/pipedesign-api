from flask import Flask
from src import create_app

# For Azure app service
app = create_app(config_name="prod")

# For easy local testing
if __name__ == '__main__':
    local_app = create_app(config_name="dev")
    local_app.run(debug=True)
