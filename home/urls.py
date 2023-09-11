from django.urls import path, include
from . import views
from django.conf import settings

urlpatterns = [
    path('hitter-report/<int:report_id>/edit', views.hitter_report_edit, name='edit hitter report'),
    path('hitter-report/<int:report_id>', views.hitter_report_view, name='hitter report'),
    path('pitcher-report/<int:report_id>', views.pitcher_report_view, name='hitter report'),
    path('hitter-report/create', views.hitter_report_add, name='add hitter report'),
    path('pitcher-report/create', views.pitcher_report_add, name='add pitcher report'),
    path('pitcher-report/<int:report_id>/edit', views.pitcher_report_edit, name='edit pitcher report'),
    path('', views.home, name='home'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(
        path('__debug__/', include(debug_toolbar.urls)),
        # ... your other URL patterns ...
    )
