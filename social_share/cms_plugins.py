from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from cms.models import Title


class SocialShare(CMSPluginBase):
	model = CMSPlugin
	name = _("Social Share")
	render_template = "social_share.html"
	cache = False
		
		
plugin_pool.register_plugin(SocialShare)