import re

SIZES = {
	'hd':'_1080p',
	'hd2':'_720p',
	'med':'_screenshot_med',
	'big':'_screenshot_big',
	'thumb':'_thumb'
}

def process_image_url(url,size):
	pre = 'http:'
	fmt_str = re.sub('_thumb',SIZES[size],url)
	full_url = pre + fmt_str
	
	return full_url

def main():
	url = '//images.igdb.com/igdb/image/upload/t_thumb/sc79cx.jpg'
	print(process_image_url(url,'hd2'))

if __name__ == '__main__':
	main()
