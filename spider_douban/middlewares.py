from spider_douban.settings import USER_AGENT_LIST
import random

class RandomUserAgentMiddleware():
    def process_request(self, request, spider):
        ua  = random.choice(USER_AGENT_LIST)
        if ua:
            request.headers.setdefault('User-Agent', ua)