from flask_restx import Namespace, fields


class PriceDto:
    api = Namespace('price', description='house price prediction operations')

    requestParser = api.parser()
    requestParser.add_argument(
        'bedrooms', required=False, type=int, default=1,
        help="Number of bedrooms in the house (default: 1)"
    ),
    requestParser.add_argument(
        'bathrooms', required=False, type=int, default=1,
        help="Number of bathrooms in the house (default: 1)"
    ),
    requestParser.add_argument(
        'sqft_living', required=False, type=int, default=1100,
        help="Living room area in square feet (default: 1000)"
    ),
    requestParser.add_argument(
        'sqft_lot', required=False, type=int, default=4500,
        help="Plot of land area in square feet (default: 4500)"
    ),
    requestParser.add_argument(
        'floors', required=False, type=float, default=2,
        help="Number of floors in the house (default: 2)"
    ),
    requestParser.add_argument(
        'waterfront', required=False, type=bool, default=False,
        help="Is the house near a waterfront location (default: False)"
    ),
    requestParser.add_argument(
        'view', required=False, type=int, default=0,
        help="Rating for the view outside the house (default: 0)"
    ),
    requestParser.add_argument(
        'condition', required=False, type=int, default=5,
        help="Rating for the overall condition of the house (default: 5)"
    ),
    requestParser.add_argument(
        'grade', required=False, type=int, default=7,
        help="Overall grade for the house (default: 7)"
    ),
    requestParser.add_argument(
        'sqft_above', required=False, type=int, default=1200,
        help="Upper floor area in square feet (default: 1200)"
    ),
    requestParser.add_argument(
        'sqft_basement', required=False, type=int, default=0,
        help="Basement area in square feet (default: 0)"
    ),
    requestParser.add_argument(
        'yr_built', required=False, type=int, default=1955,
        help="Year the house was built (default: 1955)"
    ),
    requestParser.add_argument(
        'yr_renovated', required=False, type=int, default=1956,
        help="Year of the latest renovation (default: 1956)"
    ),
    requestParser.add_argument(
        'lat', required=False, type=float, default=47.5,
        help="Latitude of the house location (default: 47.5)"
    ),
    requestParser.add_argument(
        'long', required=False, type=float, default=-122.3,
        help="Longitude of the house location (default: -122.3)"
    ),
    requestParser.add_argument(
        'sqft_living15', required=False, type=int, default=1340,
        help="Living room area of the 15 nearest neighbors (default: 1340)"
    ),
    requestParser.add_argument(
        'sqft_lot15', required=False, type=int, default=5650,
        help="Plot of land area of the 15 nearest neighbors (default: 5650)"
    ),
    requestParser.add_argument(
        'year', required=False, type=int, default=2014,
        help="Issued year (default: 2014)"
    ),
    requestParser.add_argument(
        'month', required=False, type=int, default=6,
        help="Issued month (default: 6)"
    ),
    price = api.model('user', {
        'bedrooms': fields.Integer(description='Number of bedrooms'),
        'bathrooms': fields.Integer(description='Number of bathrooms'),
        'sqft_living': fields.Integer(description='Living room area'),
        'sqft_lot': fields.Integer(description='Plot of land area'),
        'floors': fields.Integer(description='Plot of land area'),
        'waterfront': fields.Boolean(description='Is your house near a water side?'),
        'view': fields.Integer(description='Rating for the view outside'),
        'condition': fields.Integer(description='Rating for its condition'),
        'grade': fields.Integer(description='Overall grade for your house'),
        'sqft_above': fields.Integer(description='Upperfloor area'),
        'sqft_basement': fields.Integer(description='Basement area'),
        'yr_built': fields.Integer(description='Year built'),
        'yr_renovated': fields.Integer(description='Latest renovation year'),
        'lat': fields.Integer(description='Latitude of this location'),
        'long': fields.Integer(description='Longtitude of this location'),
        'sqft_living15': fields.Integer(description='Living room area of the 15 nearest neighbor'),
        'sqft_lot15': fields.Integer(description='Plot of land area of the 15 nearest neighbor'),
        'year': fields.Integer(description='Issued year'),
        'month': fields.Integer(description='Issued month'),
    })
