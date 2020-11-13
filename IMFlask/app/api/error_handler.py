'''
Flask Application Error Handler
'''
from flask import Blueprint, jsonify, request, render_template

error_handler = Blueprint('error_handler', __name__)


@error_handler.app_errorhandler(400)
def bad_requests(error):
    '''400 error handler'''
    if request.accept_mimetypes.accept_json and \
       not request.accept_mimetypes.accept_html:
        return jsonify(msg=str(error)), 400
    return "400 page", 400


@error_handler.app_errorhandler(404)
def not_found(error):
    '''404 error handler'''
    if request.accept_mimetypes.accept_json and \
       not request.accept_mimetypes.accept_html:
        return jsonify(msg=str(error)), 404
    return "404 page", 404


@error_handler.app_errorhandler(500)
def internal_server_error(error):
    '''500 error handler'''
    if request.accept_mimetypes.accept_json and \
       not request.accept_mimetypes.accept_html:
        return jsonify(msg=str(error)), 500
    return "500 Page", 500
