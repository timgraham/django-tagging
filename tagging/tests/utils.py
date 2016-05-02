"""
Tests utils for tagging.
"""
from django.template.loaders.base import Loader


class VoidLoader(Loader):
    """
    Template loader which is always returning
    an empty template.
    """
    is_usable = True
    _accepts_engine_in_init = True

    def load_template_source(self, template_name, template_dirs=None):
        return ('', 'voidloader:%s' % template_name)
