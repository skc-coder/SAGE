- [[Disable extension on certain websites]]
  [[How to create desktop shortcuts]]
  [[How to generate usernames]] 
  [[How to set a default Folder View for all folders in Windows 11]]
  [[Remove bing search from start menu]]
  [[Setting up google drive]]
  [[Telegram restricted download]]
- [[VLC FIX]]
  collapsed:: true
	- To fix VLC codec issues on Arch Linux without installing every plugin, use this minimal setup:
	- `sudo pacman -S vlc \ vlc-plugin-ffmpeg vlc-plugin-mpeg2 vlc-plugin-x264 vlc-plugin-x265 \ vlc-plugin-ass vlc-plugin-matroska vlc-plugin-dvd vlc-plugin-bluray \ vlc-plugin-srt vlc-plugin-soxr libdvdcss libbluray`
	- This setup covers most common formats like MP4, MKV, H264, HEVC, DVDs, Blu-rays, and subtitles, without pulling in unnecessary plugins.
	- https://old.reddit.com/r/archlinux/comments/1lwbm3a/vlc_media_player_problem/n6s7d4o/?context=3
	- Fedora
		- vlc-plugin-ffmpeg.x86_64
		  vlc-plugin-pause-click.x86_64
		  vlc-plugin-visualization.x86_64
		  vlc-plugins-base.x86_64
		- /## vlc-plugins-all.x86_64
		-
- [[Num lock auto on]]
-