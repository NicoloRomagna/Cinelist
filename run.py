from dotenv import load_dotenv
from app import create_app

#carico le variabili dal file .env
load_dotenv()
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)