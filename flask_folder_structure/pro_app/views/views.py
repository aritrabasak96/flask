from pro_app import app2,api,Resource
from pro_app.modules import apc as a

class FirstRoute(Resource):
    def get(self):
        t1 = a.Calculation()
        data = t1.cal()
        return str(data)

api.add_resource(FirstRoute,"/")

# @app2.route("/")
# def firstRoute():
#     t1 = a.Calculation()
#     data = t1.cal()
#     return str(data)
