from starlette_exporter import PrometheusMiddleware, handle_metrics

def setup_monitoring(app):
    app.add_middleware(PrometheusMiddleware, group_paths=True)
    app.add_route("/metrics", handle_metrics) 