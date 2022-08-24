from cloudant.client import Cloudant
from cloudant.error import CloudantException
import requests
import json


dict={
    "IAM_API_KEY":"fzgex6SI1CyZHsTrIgrGJ8PwW_hE0nnDkAm7vh3a3vf-",
    "URL":"https://e2534b0c-1d83-4882-925e-87a6cd77ba01-bluemix.cloudantnosqldb.appdomain.cloud"
}

database='reviews'
dealer_id=15

review={
        "id": 1114,
        "name": "Upkar Lidder",
        "dealership": 15,
        "review": "Great service!",
        "purchase": False,
        "another": "field",
        "purchase_date": "02/16/2021",
        "car_make": "Jaguar",
        "car_model": "Car",
        "car_year": 2025
    }


def main(dict,database,review):
    '''Should return dealerships and reviews for this example'''
    try:
        client = Cloudant.iam(
            None,
            api_key=dict["IAM_API_KEY"],
            url=dict["URL"],
            connect=True,
        )
    except CloudantException as ce:
        print("unable to connect")
        return {"error": ce}
    except (requests.exceptions.RequestException, ConnectionResetError) as err:
        print("connection error")
        return {"error": err}
    my_review= client[database].create_document(review)
    return {"review": my_review}
    

main(dict,database,review)








