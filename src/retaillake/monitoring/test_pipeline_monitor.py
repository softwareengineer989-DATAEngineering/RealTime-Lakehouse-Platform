from retaillake.monitoring.pipeline_monitor import (
    initialize_pipeline,
    shutdown_pipeline,
)

initialize_pipeline("Gold Pipeline")

shutdown_pipeline("Gold Pipeline")