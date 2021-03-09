import time
from feed_parsers.source_feed import SourceFeed
from pipeline.pipeline_stage import PipelineStage


class FeedManager(PipelineStage):

    def __init__(self, feeds: [SourceFeed]):
        super().__init__()
        self._feeds = feeds

    def start(self):
        start = time.time()
        articles = []

        for f in self._feeds:
            articles += f.fetch()

        print(f'Took: {time.time() - start}, Found: {len(articles)} new articles')
        self.emit(articles)

    def _process_one(self, to_process):
        raise NotImplementedError
