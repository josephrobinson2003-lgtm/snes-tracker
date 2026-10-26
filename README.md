# SNES Collection Tracker

Live app: https://josephrobinson2003-lgtm.github.io/snes-tracker/

Android app: [SNES-Tracker.apk](https://github.com/josephrobinson2003-lgtm/snes-tracker/releases/latest/download/SNES-Tracker.apk) — works offline with the list bundled in. iPhone: use Safari → Share → Add to Home Screen.

A simple phone-friendly checklist of 710 SNES games. Joe's owned games (the yellow cells in his spreadsheet) are the default list for everyone.

- Tap a game to switch it between Owned and Need. Changes are saved only on that phone or browser, in localStorage.
- Use **Share / Sync → Copy my owned list** and **Import** to move a list between phones. **Reset to Joe's list** goes back to the default.
- Add to Home Screen to install it like an app. The service worker loads the page and data network-first, so updates show up the next time it opens with a connection.

## Updating the game list
1. Edit `games.json` (`[{"title": "...", "owned": true/false, "letter": "A"}]`).
2. Run `python3 build.py`. It embeds the data in `index.html` and gives `sw.js` a new version, which busts the cache.
3. Commit and push. GitHub Pages redeploys in about a minute.

Edit `template.html` and `sw.template.js` instead of `index.html` and `sw.js`. Those two files are generated.
