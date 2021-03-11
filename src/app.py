from flask_restful import Api
from dotenv import load_dotenv

from app_septup import Application
from service import  Lang

app = Application.app
api = Api(app)

@app.before_first_request
def loading_config():
    print('Language api started!')

api.add_resource(Lang, '/translation/<string:pageId>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, debug=True, ssl_context='adhoc')
     
