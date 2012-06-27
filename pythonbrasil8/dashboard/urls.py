# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from pythonbrasil8.dashboard.views import IndexView, ProfileView, SessionsView
from pythonbrasil8.subscription.views import SubscriptionView
from pythonbrasil8.schedule.views import SubscribeView


urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='dashboard-index'),
    url(r'^subscription/talk/$', SubscriptionView.as_view(), name='talk-subscription'),
    url(r'^profile/$', ProfileView.as_view(), name="edit-profile"),
    url(r'^proposals/$', SessionsView.as_view(), name="dashboard-sessions"),
    url(r'^proposals/propose/$', SubscribeView.as_view(), name='session-subscribe'),
)
