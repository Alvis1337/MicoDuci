from rest_framework.exceptions import APIException


class InvalidArgumentSupplied(APIException):
    status_code = 400
    default_detail = "the supplied argument is invalid"
    default_code = "invalid_arg"


class NoArgumentSupplied(APIException):
    status_code = 400
    default_detail = "you must supply an argument for that function"
    default_code = "no_arg_supplied"
