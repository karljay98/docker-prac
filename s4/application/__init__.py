from flask import Flask, Response, request
import requests

app = Flask(__name__)

@app.route('/post/transformer', methods =['POST'])
# two get requests are needed for service 2 and 3
# use these in logic for transformers.
def get_transformer():
    transformer_car = request.data.decode('utf-8')
    transformer_split = transformer_car.split(",")
    car_list = transformer_split[1]
    colour = transformer_split[0]

    if colour == "yellow" and car_list == "Mustang":
        transformer = "Bumblebee"
    elif colour == "yellow" and car_list == "Mercedes":
        transfromer = "Jazz"
    elif colour == "yellow" and car_list == "Truck":
        transformer = "Rachet"
    elif colour == "red" and car_list == "Mercedes":
        transformer = "Hot rod"
    elif colour == "red" and car_list == "Mustang":
        transformer = "Long haul"
    elif colour == "red" and car_list == "Truck":
        transfromer = "Optimus prime"
    elif colour == "grey" and car_list == "Mercedes":
        transformer = "Slingshot"
    elif colour == "grey" and car_list == "Mustang":
        transformer = "Barricade"
    else:
        transformer = "Galvatron"

    return Response(transformer, mimetype='text/plain')
if __name__ == '__main__':
    app.run(port=5003, debug=True, host='0.0.0.0')