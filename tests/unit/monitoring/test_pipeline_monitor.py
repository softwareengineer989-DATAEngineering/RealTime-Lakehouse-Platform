from retaillake.monitoring.pipeline_monitor import PipelineMonitor


monitor = PipelineMonitor(

    "Gold Streaming"

)

monitor.startup()

monitor.metrics.increment_processed(

    100000

)

monitor.metrics.increment_invalid(

    50

)

monitor.metrics.increment_failed(

    5

)

monitor.metrics.increment_batch()

monitor.shutdown()