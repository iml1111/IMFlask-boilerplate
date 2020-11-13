'''
API rquest handler and util
'''
from flask import abort, g, current_app, request


def init_app(app):

    @app.before_first_request
    def before_first_request():
        pass

    @app.before_request
    def before_request():
        pass

    @app.after_request
    def after_request(response):

        # Slow API Tracking
        if 'process_time' in g and \
        g.process_time >= current_app.config['SLOW_API_TIME']:
            log_str = "\n!!! SLOW API DETECTED !!! \n" + \
                      "ip: " + request.remote_addr + "\n" + \
                      "url: " + request.full_path + "\n" + \
                      "input_json: " + str(request.get_json()) + "\n" + \
                      "slow time: " + str(g.process_time) + "\n"
            app.logger.warning(log_str)

        return response

    @app.teardown_request
    def teardown_request(exception):
        pass

    @app.teardown_appcontext
    def teardown_appcontext(exception):
        pass


def input_check(data, key, value_type, length=None):
    '''json input 파라미터 인자 검증 함수'''
    if key not in data:
        abort(400, description="'%s' not in data." % key)
    if not isinstance(data[key], value_type):
        abort(400, description="'%s' must be '%s' type." % (key, str(value_type)))
    if length and len(data[key]) > length:
        abort(400, description="'%s' is too long(longer than '%s')" % (key, str(length)))