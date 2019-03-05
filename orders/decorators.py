from rest_framework.response import Response
from rest_framework.views import status
import re


def validate_request_data(fn):
    def decorated(*args, **kwargs):
        phoneNumber = args[0].request.data.get("phoneNumber", "")
        email = args[0].request.data.get("email", "")
        numberPattern = re.compile("^(\+98|0)?9\d{9}$")
        emailPattern = re.compile("^ $")
        if numberPattern.match(phoneNumber):
            return Response(
                data={
                    "message": "Enter a correct Phone Number"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        if emailPattern.match(email):
            return Response(
                data={
                    "message": "Enter a correct Email"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return fn(*args, **kwargs)
    return decorated