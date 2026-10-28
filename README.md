# SNES Collection Tracker

Live app: https://josephrobinson2003-lgtm.github.io/snes-tracker/

Android app: [SNES-Tracker.apk](https://github.com/josephrobinson2003-lgtm/snes-tracker/releases/latest/download/SNES-Tracker.apk) (v1.1). Each time it opens online it loads the latest list from this site (4-second limit). Offline, it uses the last list it downloaded, or the copy built into the app. v1.0 users need to install v1.1 over it once. Their saved taps carry over. iPhone: use Safari → Share → Add to Home Screen.

A simple phone-friendly checklist of 710 SNES games. Joe's owned games (the yellow cells in his spreadsheet) are the default list for everyone.

- Tap a game to switch it between Owned and Need. Only that phone's own changes are saved (localStorage key `snes-overrides-v2`, title → owned/need). Every other game follows the latest published list, so new games and changes to Joe's list show up on every phone. Saved lists from v1.0 (`snes-owned-v1`) are converted automatically, using `owned-v1-baseline.json`.
- Use **Share / Sync → Copy my owned list** and **Import** to move a list between phones. **Reset to Joe's list** goes back to the default.
- Add to Home Screen to install it like an app. The service worker loads the page and data network-first, so updates show up the next time it opens with a connection.

## Updating the game list
1. Edit `games.json` (`[{"title": "...", "owned": true/false, "letter": "A"}]`).
2. Run `python3 build.py`. It embeds the data in `index.html` and gives `sw.js` a new version, which busts the cache.
3. Commit and push. GitHub Pages redeploys in about a minute. The web/iPhone version and the Android app (v1.1+) pick up the new list the next time they open online. No new APK is needed.

Only rebuild the APK (`android/build-apk.sh`, same keystore, bump `versionCode`) when the Android wrapper itself changes.

Edit `template.html` and `sw.template.js` instead of `index.html` and `sw.js`. Those two files are generated.
