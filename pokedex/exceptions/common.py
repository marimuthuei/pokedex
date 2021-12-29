class DomainException(Exception):
    code = "domain_exception"


class NotFoundError(DomainException):
    code = "not_found_error"


