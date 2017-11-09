


class AppManager(object):

   def __init__(self):
      pass


   def add_app(self, app_name, default_limits=None, static_path=None):
      pass

   def add_app_conf(self, app_conf):
      '''
      app_conf = {
         'app_name' : 'required',
         'default_limits' : 'optional',
         'limits_filter' : <filter_func>, #if returns true, does not perform limit check

         'accepts' : ['head', 'get', 'post'],

         'conf_modifier' : <get_final_conf/conf_modifier_func>, #default is None

         'static_urls' : [ #optional
            { 'name' : 'url_var_name2'
              'url' : 'route_url', #url in flask
              'path' : 'path', #actual path on disk relative to the app group root
              'is_exposed' : Bool #can other apps use it?
            },
            {
               'name' : 'url_var_name2',
               ...
            }
            #'base_url' : 'actual_path',
            #'base_url2' : 'actual_path'
         ],

         'dynamic_urls' : [ #same as add_path
            { 'url' : 'base_url', #either use url or urls, not both
              'urls' : ['list_urls'],
              'view_func' : view_function,
              'prior' : <priority>,
              'limit' : <limit>,
              'conf_modifier' : get_final_conf
            },
            { ... }
         ],

         'templates' : [
            { 'name' : '<temp_name>',
              'is_relative' : Bool, #if true, only need filename for path, otherwise app group path
              'is_exposed' : Bool, #can other apps use it?
              'path' : '<filename/app group path>',
            },
             { ... }
         ]

      }
      '''

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

