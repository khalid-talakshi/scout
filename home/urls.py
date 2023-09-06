from django.urls import path, include
from . import views
from django.conf import settings

urlpatterns = [
    path('hitter-report/<int:report_id>', views.hitter_report_view, name='hitter report'),
    path('hitter-report/create', views.hitter_report_add, name='add hitter report'),
    path('', views.home, name='home'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(
        path('__debug__/', include(debug_toolbar.urls)),
        # ... your other URL patterns ...
    )
