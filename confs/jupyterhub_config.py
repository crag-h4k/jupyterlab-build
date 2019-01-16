# Configuration file for jupyter-notebook.
c.NotebookApp.certfile = u'/PATH_TO.pem'
c.NotebookApp.keyfile = u'/PATH_TO_.pem'
c.NotebookApp.open_browser = False

c.NotebookApp.password = u''
c.NotebookApp.allow_remote_access = True
c.NotebookApp.ip = '*'
c.NotebookApp.port = 1234
c.NotebookApp.base_url = u'/'
c.NotebookApp.default_url = '/lab'
c.Spawner.default_url = '/lab'
#------------------------------------------------------------------------------
"""
c.JupyterHub.authenticator_class = 'ldapauthenticator.LDAPAuthenticator'
c.LDAPAuthenticator.bind_dn_template = [
    "uid={username},ou=people,dc=wikimedia,dc=org",
    "uid={username},ou=developers,dc=wikimedia,dc=org",
]
#Active directory options
c.LDAPAuthenticator.lookup_dn = True
c.LDAPAuthenticator.lookup_dn_search_filter = '({login_attr}={login})'
c.LDAPAuthenticator.lookup_dn_search_user = 'ldap_search_user_technical_account'
c.LDAPAuthenticator.lookup_dn_search_password = 'secret'
c.LDAPAuthenticator.user_search_base = 'ou=people,dc=wikimedia,dc=org'
c.LDAPAuthenticator.user_attribute = 'sAMAccountName'
c.LDAPAuthenticator.lookup_dn_user_dn_attribute = 'cn'
c.LDAPAuthenticator.escape_userdn = False
#additional options
c.LDAPAuthenticator.valid_username_regex
c.LDAPAuthenticator.use_ssl = True
c.LDAPAuthenticator.server_port =

c.LDAPAuthenticator.search_base
c.LDAPAuthenticator.user_attribute
"""
