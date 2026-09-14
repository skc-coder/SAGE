```
REG ADD HKCU\Software\Microsoft\Windows\CurrentVersion\Search /v BingSearchEnabled /t REG_DWORD /d 0 
REG ADD HKCU\Software\Microsoft\Windows\CurrentVersion\Search /v CortanaConsent /t REG_DWORD /d 0 
tskill searchui
```

https://www.reddit.com/r/Windows10/comments/f09184/how_to_block_bing_search_in_windows_10_start_menu/