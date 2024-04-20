from flask import request
from flask_restx import Resource

from src.modules.price.dto import PriceDto

from src.modules.price.service import predictHousePriceUsingANN, predictHousePriceUsingLR

api = PriceDto.api
requestDto = PriceDto.requestParser
priceDto = PriceDto.price


@api.route('/predict')
class PricePredict(Resource):

    @api.expect(requestDto)
    def get(self):
        args = request.args.to_dict(flat=True)
        modelType = args.pop('model', None)
        params = [float(False if value == 'false' else True if value == 'true' else value)
                  for key, value in args.items()]
        # predict = model.predict(a)

        if (modelType == 'ann'):
            predict = predictHousePriceUsingANN(params)
            return {'price': float(predict)}

        if (modelType == 'linear'):
            predict = predictHousePriceUsingLR(params)
            print(predict)
            return {'price': float(predict)}
