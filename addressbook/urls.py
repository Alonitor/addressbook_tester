# from django.conf.urls import patterns, url
from django.conf.urls import url
from django.urls import path, include
from . import views

# urlpatterns = patterns('addressbook.views',
#     url(r'^$', 'index', name='addressbook_index'),
#
#     url(r'^group/add$', 'add_group', name='addressbook_add_group'),
#
#     url(r'^contact/add$', 'add_contact', name='addressbook_add_contact'),
#     url(r'^contact/(?P<pk>\d+)/edit$', 'edit_contact',
#             name='addressbook_edit_contact'),
#     url(r'^contact/(?P<pk>\d+)/view$', 'single_contact',
#             name='addressbook_single_contact'),
#     url(r'^contact/(?P<pk>\d+)/download$', 'download_vcard',
#             name='addressbook_download_vcard'),
# )

# urlpatterns = [
#     path(addressbook.views),
#     url(r'^$', 'index', name='addressbook_index'),
#
#     url(r'^group/add$', 'add_group', name='addressbook_add_group'),
#
#     url(r'^contact/add$', 'add_contact', name='addressbook_add_contact'),
#     url(r'^contact/(?P<pk>\d+)/edit$', 'edit_contact',
#             name='addressbook_edit_contact'),
#     url(r'^contact/(?P<pk>\d+)/view$', 'single_contact',
#             name='addressbook_single_contact'),
#     url(r'^contact/(?P<pk>\d+)/download$', 'download_vcard',
#             name='addressbook_download_vcard'),
# ]

app_name = 'addressbook'

urlpatterns = [
    path('index/', views.index, name='addressbook_index'),

    path('add_group/', views.add_group, name='addressbook_add_group'),

    path('add_contact/', views.add_contact, name='addressbook_add_contact'),
    path('edit_contact/', views.edit_contact, name='addressbook_edit_contact'),
    path('<int:pk>/view', views.single_contact, name='addressbook_single_contact'),
    path('<int:pk>/download', views.download_vcard, 'download_vcard', name='addressbook_download_vcard'),
]
