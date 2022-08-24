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


dict={
    "IAM_API_KEY":"fzgex6SI1CyZHsTrIgrGJ8PwW_hE0nnDkAm7vh3a3vf-",
    "URL":"https://e2534b0c-1d83-4882-925e-87a6cd77ba01-bluemix.cloudantnosqldb.appdomain.cloud"
}



def main(dict):
    '''Should return dealerships and reviews for this example'''

    try:
        client = Cloudant.iam(
            None,
            api_key=dict["IAM_API_KEY"],
            url=dict["URL"],
            connect=True,
        )
        print("Databases: {0}".format(client.all_dbs()))
    except CloudantException as ce:
        print("unable to connect")
        return {"error": ce}
    except (requests.exceptions.RequestException, ConnectionResetError) as err:
        print("connection error")
        return {"error": err}

    return {"dbs": client.all_dbs()}


main(dict)