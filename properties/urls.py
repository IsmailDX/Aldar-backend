from django.urls import path
from . import views

urlpatterns = [
    path("allProperties/", views.property_list),
    path(
        "allProperties/<str:id>/",
        views.property_list_by_id,
        name="property-list-by-id",
    ),
    path(
        "propertiesByLocation/<str:location>/",
        views.property_list_by_location,
        name="property-list-by-location",
    ),
    path(
        "propertiesByProject/<str:project>/",
        views.property_list_by_project,
        name="property-list-by-project",
    ),
    path(
        "propertiesByBedrooms/<int:bedrooms>/",
        views.property_list_by_bedrooms,
        name="property-list-by-bedrooms",
    ),
    path(
        "propertiesByBedroomsAndProject/<str:project>/<int:bedrooms>",
        views.property_list_by_bedrooms_and_project,
        name="property-list-by-bedrooms-and-project",
    ),
    path(
        "propertiesByBedroomsAndlocation/<str:location>/<int:bedrooms>",
        views.property_list_by_bedrooms_and_location,
        name="property-list-by-bedrooms-and-location",
    ),
]
