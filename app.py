from flask import Flask, request
from flask_restplus import Resource, Api
import json
from pymongo import MongoClient
import qrcode
from constant import MONGO_URI
import uuid

app = Flask(__name__)
api = Api(app)

MONGODB_URI = MONGO_URI
client = MongoClient(MONGODB_URI, connectTimeoutMS=30000)
db = client.get_database("trs")

queryParser = api.parser()
queryParser.add_argument('claim_id')

@api.route('/TRSclaim')
@api.expect(queryParser)
class TRSclaim(Resource):
    def get(self):

        args = queryParser.parse_args()
        claim_id = args.get('claim_id')

        claimsCollection = db['claims']
        document={}
        document['found']="False"

        if (claimsCollection.find_one({"claim_id": claim_id}) != None):
            document = claimsCollection.find_one({"claim_id": claim_id})
            document['_id'] = str(document['_id'])
            document['found']="True"
            return document, 200
        else:
            return document, 200

    def post(self):

        data = request.json
        data['claim_id'] = str(uuid.uuid4())

        claimsCollection = db['claims']
        inserted_claim = claimsCollection.insert_one(data)

        

        return {'claim_id': data['claim_id']}

if __name__ == '__main__':
    # app.run(host='0', port=8007, debug=True)
    app.run(debug=True)


## QR code 

    # qr = qrcode.QRCode(
    #     version=1,
    #     error_correction=qrcode.constants.ERROR_CORRECT_L,
    #     box_size=10,
    #     border=4,
    # )

    # qr.add_data(inserted_claim.inserted_id)
    # qr.make(fit=True)

    # img = qr.make_image(fill_color="black", back_color="white")
    # img.save("image.jpg")