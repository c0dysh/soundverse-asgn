from starlette_exporter import PrometheusMiddleware, handle_metrics
from prometheus_client import Counter

# Custom metrics
clip_view_counter = Counter(
    'clip_views_total',
    'Total number of times a clip has been streamed',
    ['clip_id', 'genre']
)
clip_create_counter = Counter(
    'clip_creates_total',
    'Total number of clips created',
    ['genre']
)

def setup_monitoring(app):
    app.add_middleware(PrometheusMiddleware, group_paths=True)
    app.add_route("/metrics", handle_metrics) 