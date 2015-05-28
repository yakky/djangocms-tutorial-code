from django.db import models
from cms.models import CMSPlugin
from polls.models import Poll


class PollPlugin(CMSPlugin):
    poll = models.ForeignKey(Poll)

    def __unicode__(self):
        return self.poll.question
