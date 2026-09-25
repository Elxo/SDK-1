# Module 1 — System Map

## a. Diagram

TODO

## b. Request trace

TODO

## c. Environment gotchas

The first `docker compose up --build` finished in ~3 min. A plain `docker compose up`
(no rebuild) finished in ~35 sec. No errors were thrown and all containers came up
healthy.

**Expected:** Vite's dev server should hot-reload the page when I save a file
in `frontend/src/`. The browser keeps a WebSocket open to
`ws://localhost:5173/?token=…` for exactly this.

**What happened:** I changed the text "Frontend is running successfully!" in
`frontend/src/main.js` and saved. The page didn't update, and the WebSocket's
Messages tab showed only the initial `connected` message. Pressing F5 didn't
help either: the old text stayed.

**How I narrowed it down:**
1. `docker compose exec frontend grep -n "running" src/main.js` showed the
   **new** text, so the bind mount (`./frontend:/app`) was syncing the file
   into the container correctly.
2. In the Network tab, `main.js` came back with status **304 Not Modified**,
   and the Response still contained the **old** text. So it was not the
   browser's cache: the browser asked whether the file had changed, and Vite
   answered "no".
3. No update message ever arrived on the WebSocket.

Conclusion: the file changed on disk, but Vite never received a file-change
notification, so it kept serving its cached, already-processed copy.

## d. Documentation drift

TODO
