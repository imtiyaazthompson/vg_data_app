import re

class IGDBvideo:

	PREPEND = "https://www.youtube.com/watch?v="

	def __init__(self,vid):
		self.id = vid
	
	def get_url(self):
		return self.PREPEND + self.id

class IGDBimage:

	PREPEND = "http:"

	def __init__(self,url):
		self.url = re.sub('_thumb','{}',url)

	def get_thumbnail(self):
		return self.PREPEND + self.url.format('_thumb')

	def get_medium(self):
		return self.PREPEND + self.url.format('_screenshot_med')

	def get_big(self):
		return self.PREPEND + self.url.format('_screenshot_big')

	def get_720p(self):
		return self.PREPEND + self.url.format('_720p')

	def get_1080p(self):
		return self.PREPEND + self.url.format('_1080p')
