
Feature: Turns status table endpoint
    As a consumer, I want an endpoint able to retrieve turns status table in the context of an application

    Background:
        Given a request url "/api/v1/serviceturns/status-table"

    Scenario: Retrieve turns status table success
        Given a device and user code have been obtained for scope "read_serviceturns"
        And the device has been authorized
        And access token has been obtained
        When the request sends "GET"
        Then the response status is "HTTP_200_OK"
        And the response property "[0].ticketNumber" is equal to "DS-SA-5"
        And the response property "[1].ticketNumber" is equal to "DS-SA-6"
        And the response property "[2].ticketNumber" is equal to "DS-SA-3"
        And the response property "[3].ticketNumber" is equal to "DS-SA-4"


    Scenario: Retrieve turns status table invalid token
        Given a device and user code have been obtained for scope "read_serviceturns"
        And the device has been authorized
        And access token has been obtained
        And access token is invalid
        When the request sends "GET"
        Then the response status is "HTTP_401_UNAUTHORIZED"


    Scenario: Retrieve turns status table unexpected scope
        Given a device and user code have been obtained for scope "write_serviceturns"
        And the device has been authorized
        And access token has been obtained
        When the request sends "GET"
        Then the response status is "HTTP_403_FORBIDDEN"