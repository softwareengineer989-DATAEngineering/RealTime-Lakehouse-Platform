from pyspark.sql.streaming import StreamingQueryListener


class BronzeListener(StreamingQueryListener):

    def onQueryStarted(self, event):
        print("=" * 80)
        print("STREAM STARTED")
        print(event.id)
        print("=" * 80)

    def onQueryProgress(self, event):
        print("=" * 80)
        print("STREAM PROGRESS")
        print(event.progress)
        print("=" * 80)

    def onQueryTerminated(self, event):
        print("=" * 80)
        print("STREAM TERMINATED")
        print(event.exception)
        print("=" * 80)