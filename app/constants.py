"""General Constants of the project
"""

BEARER_PORTION = "Bearer "
IS_AUTHORIZED_PROPERTY = "isAuthorized"
IS_VALID_PROPERTY = "isValid"
SCOPE_PROPERTY = "scope"
SCOPES_SEPARATOR = " "
EMPTY_VALUE = ""
TIMEOUT = 10

CONTENT_TYPE_JSON = "application/json"


# Device Token Auth
READ_SERVICE_TURNS_SCOPE = "read_serviceturns"

DEVICE_TOKEN_GRANT_TYPE = "urn:ietf:params:oauth:grant-type:device_code"
REFRESH_TOKEN_GRANT_TYPE = "refresh_token"
DEVICE_TOKEN_SCOPES = (READ_SERVICE_TURNS_SCOPE,)

# API Metadata
API_TITLE = "QMS Display API"
API_SUMMARY = "API for QMS Display App"
API_DESCRIPTION = "The API for the QMS Display Application."
API_VERSION = "1.0.0"

# API routes prefixes
AUTH_ROUTE_PREFIX = "/api/v1/auth"
SERVICE_TURNS_ROUTE_PREFIX = "/api/v1/serviceturns"

# CORS
ALLOWED_ORIGINS = [
    "http://localhost",
    "http://localhost:8081",
    "http://localhost:8082",
]

ALLOWED_METHODS = ["*"]
ALLOWED_HEADERS = ["*"]


# Environment names
AUTH_API_BASE_URL_ENV_NAME = "AUTH_API_BASE_URL"
APP_CLIENT_ID_ENV_NAME = "APP_CLIENT_ID"
APP_CLIENT_SECRET_ENV_NAME = "APP_CLIENT_SECRET"
IAM_API_KEY_ENV_NAME = "IAM_API_KEY"
CORE_API_KEY_ENV_NAME = "CORE_API_KEY"
CORE_API_BASE_URL_ENV_NAME = "CORE_API_BASE_URL"
TEST_AUTH_APPLICATION_ENV_NAME = "TEST_AUTH_APPLICATION"
TEST_AUTH_USERNAME_ENV_NAME = "TEST_AUTH_USERNAME"
TEST_AUTH_PASSWORD_ENV_NAME = "TEST_AUTH_PASSWORD"


# Errors
INTERNAL_SERVER_ERROR_MESSAGE = "Internal Server Error"
INTERNAL_SERVER_ERROR_CODE = "INTERNAL_SERVER_ERROR"

INVALID_TOKEN_ERROR_MESSAGE = "Invalid token"
INVALID_TOKEN_ERROR_CODE = "INVALID_TOKEN"

FORBIDDEN_ERROR_MESSAGE = "Forbidden"
FORBIDDEN_ERROR_CODE = "FORBIDDEN_ACCESS"

UNAUTHORIZED_ERROR_MESSAGE = "Unauthorized"
UNAUTHORIZED_ERROR_CODE = "UNAUTHORIZED"

BAD_REQUEST_ERROR_CODE = "BAD_REQUEST"

INTERNAL_ERROR_TYPE = "INTERNAL_ERROR"
AUTHORIZATION_ERROR_TYPE = "AUTHORIZATION_ERROR"
VALIDATION_ERROR_TYPE = "VALIDATION_ERROR"



# API statuses description
HTTP_400_DESCRIPTION = "Client is sending an incorrect format of API request"
HTTP_401_DESCRIPTION = "Client is not authenticated against the API"
HTTP_403_DESCRIPTION = "Client doesn't have permission to request this resource"
HTTP_404_DESCRIPTION = "Resource could not be found"
HTTP_422_DESCRIPTION = (
    "The server was unable to process the request because it contains invalid data"
)
HTTP_500_DESCRIPTION = "Unexpected internal error"
