#
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
#
from cloudant.client import Cloudant
from cloudant.error import CloudantException
import requests
import json


dict={
    "IAM_API_KEY":"fzgex6SI1CyZHsTrIgrGJ8PwW_hE0nnDkAm7vh3a3vf-",
    "URL":"https://e2534b0c-1d83-4882-925e-87a6cd77ba01-bluemix.cloudantnosqldb.appdomain.cloud"
}

# database='dealerships'
database='reviews'


def main(dict,database):
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
    json_result= json.dumps(result)
    return json_result


print(main(dict,database))