class UrlManager:

    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def has_new_url(self):
        return self.new_url_size() != 0

    def set_old_url(self, url):

        if url is None:
            return

        if url not in self.old_urls:
            self.old_urls.add(url)

    def set_new_url(self, url):

        if url is None:
            return

        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def set_new_urls(self, urls):
        '''

        :param urls:
        :return:
        '''
        if urls is None or len(urls) == 0:
            return

        for url in urls:
            self.new_urls.add(url)

    def get_new_url(self):
        url = self.new_urls.pop()
        self.set_old_url(url)
        return url

    def new_url_size(self):
        '''
        :return:  url size
        '''
        return len(self.new_urls)

    def old_url_size(self):
        return len(self.old_urls)
