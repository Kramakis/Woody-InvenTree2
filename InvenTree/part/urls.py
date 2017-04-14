from django.conf.urls import url, include

from . import views

""" URL patterns associated with part categories:
/category       -> List all top-level categories
/category/<pk>  -> Detail view of given category
/category/new   -> Create a new category
"""
categorypatterns = [

    # Part category detail
    url(r'^category/(?P<pk>[0-9]+)/$', views.PartCategoryDetail.as_view()),

    # List of top-level categories
    url(r'^$', views.PartCategoryList.as_view())
]

partparampatterns = [
    # Detail of a single part parameter
    url(r'^(?P<pk>[0-9]+)/$', views.PartParamDetail.as_view()),

    # Parameters associated with a particular part
    url(r'^\?[^/]*/$', views.PartParamList.as_view()),

    # All part parameters
    url(r'^$', views.PartParamList.as_view()),
]

parttemplatepatterns = [
    # Detail of a single part field template
    url(r'^(?P<pk>[0-9]+)/$', views.PartTemplateDetail.as_view()),

    # List all part field templates
    url(r'^$', views.PartTemplateList.as_view())

]

""" Top-level URL patterns for the Part app:
/part/          -> List all parts
/part/new       -> Create a new part
/part/<pk>      -> (refer to partdetailpatterns)
/part/category  -> (refer to categorypatterns)
"""
urlpatterns = [
    # Individual part
    url(r'^(?P<pk>[0-9]+)/$', views.PartDetail.as_view()),

    # Part categories
    url(r'^category/', views.PartCategoryList.as_view()),

    # Part parameters
    url(r'^parameters/', include(partparampatterns)),

    # Part templates
    url(r'^templates/', include(parttemplatepatterns)),

    # List parts with optional filters
    url(r'^\?*[^/]*/?$', views.PartList.as_view()),
]
