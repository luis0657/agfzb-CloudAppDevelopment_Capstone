from cloudant.client import Cloudant
from cloudant.error import CloudantException
import requests
import json


dict={
    "IAM_API_KEY":"fzgex6SI1CyZHsTrIgrGJ8PwW_hE0nnDkAm7vh3a3vf-",
    "URL":"https://e2534b0c-1d83-4882-925e-87a6cd77ba01-bluemix.cloudantnosqldb.appdomain.cloud"
}

database='dealerships'
# database='reviews'
state='TX'

def main(dict,database,state):
    '''Should return dealerships and reviews for this example'''
    result=[]
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
    for document in client[database]:
        result.append(document)


    # Retrieve documents where the name field is 'foo'
    selector = {'st': {'$eq': state}}
    docs = client[database].get_query_result(selector)
    for doc in docs:
        print(doc)
    return docs

main(dict,database,state)








