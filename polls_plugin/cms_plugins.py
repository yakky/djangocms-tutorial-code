#-*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from polls_plugin.models import PollPlugin
from django.utils.translation import ugettext as _


class CMSPollPlugin(CMSPluginBase):
    model = PollPlugin  # model where plugin data are saved
    module = _("Polls")
    name = _("Poll Plugin")  # name of the plugin in the interface
    render_template = "djangocms_polls/poll_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(CMSPollPlugin)  # register the plugin

