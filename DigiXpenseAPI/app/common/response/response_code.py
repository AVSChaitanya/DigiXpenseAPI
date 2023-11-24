#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from enum import Enum


class CustomCodeBase(Enum):
    """Custom status code base class"""

    @property
    def code(self):
        """
        Get status code
        """
        return self.value[0]

    @property
    def msg(self):
        """
        Get status code information
        """
        return self.value[1]


class CustomResponseCode(CustomCodeBase):
    """Custom response status code"""

    HTTP_200 = (200, 'Request successful')
    HTTP_201 = (201, 'New request successful')
    HTTP_202 = (202, 'The request was accepted, but processing has not yet completed')
    HTTP_204 = (204, 'The request was successful but no content was returned')
    HTTP_400 = (400, 'Request error')
    HTTP_401 = (401, 'unauthorized')
    HTTP_403 = (403, 'No Access')
    HTTP_404 = (404, 'The requested resource does not exist')
    HTTP_410 = (410, 'The requested resource has been permanently deleted')
    HTTP_422 = (422, 'The request parameter is illegal')
    HTTP_425 = (425, 'The request cannot be performed because the server cannot satisfy the request')
    HTTP_429 = (429, 'Too many requests, server limit')
    HTTP_500 = (500, 'Server internal error')
    HTTP_502 = (502, 'Gateway error')
    HTTP_503 = (503, 'The server is temporarily unable to process the request')
    HTTP_504 = (504, 'Gateway timeout')


class CustomErrorCode(CustomCodeBase):
    """Custom error status code"""

    CAPTCHA_ERROR = (40001, 'Verification code error')


class StandardResponseCode:
    """Standard response status code"""

    """
    HTTP codes
    See HTTP Status Code Registry:
    https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml

    And RFC 2324 - https://tools.ietf.org/html/rfc2324
    """
    HTTP_100 = 100 # CONTINUE: Continue
    HTTP_101 = 101 # SWITCHING_PROTOCOLS: protocol switching
    HTTP_102 = 102 # PROCESSING: Processing
    HTTP_103 = 103 # EARLY_HINTS: Hint information
    HTTP_200 = 200 # OK: Request successful
    HTTP_201 = 201 # CREATED: Created
    HTTP_202 = 202 # ACCEPTED: Accepted
    HTTP_203 = 203 # NON_AUTHORITATIVE_INFORMATION: Non-authoritative information
    HTTP_204 = 204 # NO_CONTENT: No content
    HTTP_205 = 205 # RESET_CONTENT: Reset content
    HTTP_206 = 206 # PARTIAL_CONTENT: Partial content
    HTTP_207 = 207 # MULTI_STATUS: Multiple status
    HTTP_208 = 208 # ALREADY_REPORTED: Reported
    HTTP_226 = 226 # IM_USED: used
    HTTP_300 = 300 # MULTIPLE_CHOICES: multiple choices
    HTTP_301 = 301 # MOVED_PERMANENTLY: Move permanently
    HTTP_302 = 302 # FOUND: Temporary move
    HTTP_303 = 303 # SEE_OTHER: See other locations
    HTTP_304 = 304 # NOT_MODIFIED: Not modified
    HTTP_305 = 305 # USE_PROXY: Use proxy
    HTTP_307 = 307 # TEMPORARY_REDIRECT: Temporary redirect
    HTTP_308 = 308 # PERMANENT_REDIRECT: Permanent redirect
    HTTP_400 = 400 # BAD_REQUEST: Request error
    HTTP_401 = 401 # UNAUTHORIZED: Unauthorized
    HTTP_402 = 402 # PAYMENT_REQUIRED: Payment required
    HTTP_403 = 403 # FORBIDDEN: Access forbidden
    HTTP_404 = 404 # NOT_FOUND: Not found
    HTTP_405 = 405 # METHOD_NOT_ALLOWED: Method not allowed
    HTTP_406 = 406 # NOT_ACCEPTABLE: Not acceptable
    HTTP_407 = 407 # PROXY_AUTHENTICATION_REQUIRED: Proxy authentication required
    HTTP_408 = 408 # REQUEST_TIMEOUT: Request timeout
    HTTP_409 = 409 # CONFLICT: Conflict
    HTTP_410 = 410 # GONE: Deleted
    HTTP_411 = 411 # LENGTH_REQUIRED: Content length required
    HTTP_412 = 412 # PRECONDITION_FAILED: Prerequisite failed
    HTTP_413 = 413 # REQUEST_ENTITY_TOO_LARGE: The request entity is too large
    HTTP_414 = 414 # REQUEST_URI_TOO_LONG: The request URI is too long
    HTTP_415 = 415 # UNSUPPORTED_MEDIA_TYPE: Unsupported media type
    HTTP_416 = 416 # REQUESTED_RANGE_NOT_SATISFIABLE: The request range does not meet the requirements
    HTTP_417 = 417 # EXPECTATION_FAILED: Expectation failed
    HTTP_418 = 418 # UNUSED: idle
    HTTP_421 = 421 # MISDIRECTED_REQUEST: Misdirected request
    HTTP_422 = 422 # UNPROCESSABLE_CONTENT: Unable to process the entity
    HTTP_423 = 423 # LOCKED: locked
    HTTP_424 = 424 # FAILED_DEPENDENCY: Dependency failed
    HTTP_425 = 425 # TOO_EARLY: too early
    HTTP_426 = 426 # UPGRADE_REQUIRED: Need to upgrade
    HTTP_427 = 427 # UNASSIGNED: Not allocated
    HTTP_428 = 428 # PRECONDITION_REQUIRED: Prerequisites required
    HTTP_429 = 429 # TOO_MANY_REQUESTS: Too many requests
    HTTP_430 = 430 # Unassigned: Not assigned
    HTTP_431 = 431 # REQUEST_HEADER_FIELDS_TOO_LARGE: The request header field is too large
    HTTP_451 = 451 # UNAVAILABLE_FOR_LEGAL_REASONS: Unavailable for legal reasons
    HTTP_500 = 500 # INTERNAL_SERVER_ERROR: Server internal error
    HTTP_501 = 501 # NOT_IMPLEMENTED: Not implemented
    HTTP_502 = 502 # BAD_GATEWAY: Bad gateway
    HTTP_503 = 503 # SERVICE_UNAVAILABLE: The service is unavailable
    HTTP_504 = 504 # GATEWAY_TIMEOUT: Gateway timeout
    HTTP_505 = 505 # HTTP_VERSION_NOT_SUPPORTED: HTTP version is not supported
    HTTP_506 = 506 # VARIANT_ALSO_NEGOTIATES: Variants will also be negotiated
    HTTP_507 = 507 # INSUFFICIENT_STORAGE: Insufficient storage space
    HTTP_508 = 508 # LOOP_DETECTED: Loop detected
    HTTP_509 = 509 # UNASSIGNED: Not allocated
    HTTP_510 = 510 # NOT_EXTENDED: Not extended
    HTTP_511 = 511 # NETWORK_AUTHENTICATION_REQUIRED: Network authentication required

    """
    WebSocket codes
    https://www.iana.org/assignments/websocket/websocket.xml#close-code-number
    https://developer.mozilla.org/en-US/docs/Web/API/CloseEvent
    """
    WS_1000 = 1000 # NORMAL_CLOSURE: Normally closed
    WS_1001 = 1001 # GOING_AWAY: Leaving
    WS_1002 = 1002 # PROTOCOL_ERROR: Protocol error
    WS_1003 = 1003 # UNSUPPORTED_DATA: Unsupported data type
    WS_1005 = 1005 # NO_STATUS_RCVD: No status received
    WS_1006 = 1006 #ABNORMAL_CLOSURE: Abnormal shutdown
    WS_1007 = 1007 # INVALID_FRAME_PAYLOAD_DATA: Invalid frame payload data
    WS_1008 = 1008 # POLICY_VIOLATION: Policy violation
    WS_1009 = 1009 # MESSAGE_TOO_BIG: The message is too big
    WS_1010 = 1010 # MANDATORY_EXT: required extension
    WS_1011 = 1011 # INTERNAL_ERROR: Internal error
    WS_1012 = 1012 # SERVICE_RESTART: Service restart
    WS_1013 = 1013 # TRY_AGAIN_LATER: Please try again later
    WS_1014 = 1014 # BAD_GATEWAY: Wrong gateway
    WS_1015 = 1015 # TLS_HANDSHAKE: TLS handshake error
    WS_3000 = 3000 # UNAUTHORIZED: Unauthorized
    WS_3003 = 3003 # FORBIDDEN: Access forbidden
