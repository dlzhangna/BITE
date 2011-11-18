#!/usr/bin/python2.4
#
# Copyright 2010 Google Inc. All Rights Reserved.

"""Bite home handler."""

__author__ = 'phu@google.com (Po Hu)'

#Import not at top
#pylint: disable-msg=C6204
#Statement before imports
#pylint: disable-msg=C6205
#Invalid method name
#pylint: disable-msg=C6409
try:
  import auto_import_fixer
except ImportError:
  pass

import os
import sys

try:
  from google.appengine.api import users
  from google.appengine.ext import webapp
  from google.appengine.ext.webapp.util import run_wsgi_app
  from handlers import base
except ImportError:
  file_dir = os.path.dirname(__file__)
  project_dir = os.path.join(file_dir, '..')
  sys.path.append(project_dir)
  from google.appengine.api import users
  from google.appengine.ext import webapp
  from google.appengine.ext.webapp.util import run_wsgi_app
  from handlers import base


class Error(Exception):
  pass


class TestSuiteHandler(base.BaseHandler):
  """Test Suite Handler."""

  def get(self):
    user = users.get_current_user()
    if not user:
      self.redirect(users.create_login_url(self.request.uri))
    self.RenderTemplate('suite_test.html', {})


class TestAddTestsHandler(base.BaseHandler):
  """Test add tests Handler."""

  def get(self):
    user = users.get_current_user()
    if not user:
      self.redirect(users.create_login_url(self.request.uri))
    self.RenderTemplate('add_tests.html', {})


application = webapp.WSGIApplication(
    [('/testing/suite_test', TestSuiteHandler),
     ('/testing/add_tests', TestAddTestsHandler)],
    debug=True)


def main():
  run_wsgi_app(application)


if __name__ == '__main__':
  main()