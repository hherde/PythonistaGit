#!python3

'''
This widget script shows thumbnails of photos that were recently added to the photo library.

Tapping the widget opens the Photos app.
'''

import appex
import ui
import photos

def widget_tapped(sender):
	import webbrowser
	webbrowser.open('photos-redirect://')

album = photos.get_recently_added_album()
if album:
	assets = album.assets[-6:]
	v = ui.View(frame=(0, 0, 300, 110))
	for i, a in enumerate(reversed(assets)):
		img_view = ui.ImageView(frame=(8 + i * 90, 15, 80, 80), flex='tb')
		img_view.content_mode = ui.CONTENT_SCALE_ASPECT_FILL
		img_view.image = a.get_ui_image(size=(120, 120), crop=True)
		v.add_subview(img_view)
	tap_button = ui.Button(frame=v.bounds, flex='wh', action=widget_tapped)
	v.add_subview(tap_button)
	appex.set_widget_view(v)
else:
	appex.set_widget_view(None)
	print('Cannot access photos')

