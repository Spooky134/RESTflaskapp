from app import app_init
import os
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = app_init()

if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG'),
            host=os.getenv('HOST'),
            port=app.config('PORT'))
