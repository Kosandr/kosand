


class AppManager(object):

   def __init__(self):
      pass


   def add_app(self, app_name, default_limits=None, static_path=None):
      pass

   def add_app_conf(self, app_conf):
      self.app_name = app_conf['app_name']

      pass



   def add_path(self, urls, page_view_func, app_name=None, prior=None, limit=None, conf_modifier=None):
      '''
      #bad args to page_view_func = page_view_func(app, flask_req)

      args to page_view_func =
      def page_view_func(**url_args, *etc, conf = {
                                             'template_conf' : template_conf = {
                                                'root' : 'site_root_path',
                                                'domain' : 'site_domain',
                                                'is_mobile' : is_mobile
                                             }
                                             'template_path' : <path_to_view_template>,

                                             'req' : flask_request,
                                             'sess' : flask_session,

                                             'flask_app' : flask_app, #TODO: is this needed?
                                             'app_manager' : app_manager, #TODO: is this needed?

                                             'is_post' : is_post,
                                             'is_get' : is_get,
                                             'is_head' : is_head,

                                           })

      TODO: how is this class gonna be used? do we need app_name in add_path?
      '''
      pass


   def render_template(self, name, *args, **kwargs):
      pass

   pass

