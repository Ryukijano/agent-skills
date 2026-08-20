# PCOS WebSocket Bridge

The PCOS broker acts as a WebSocket relay hub between Chrome extension and Android app.

## Architecture

```
Chrome Extension ←→ Broker (WS /bridge) ←→ Android App
                     │
                     ├── Authentication (token)
                     ├── Heartbeat (ping/pong)
                     ├── Client registration
                     └── Message relay
```

## Message Types

| Type | Direction | Purpose |
|------|-----------|---------|
| `register` | Client→Broker | Register as Chrome or Android client |
| `relay` | Client→Broker | Relay message to the other platform |
| `result` | Client→Broker | Send execution result back |
| `ping` | Client→Broker | Keepalive ping |
| `pong` | Broker→Client | Keepalive response |

## Chrome MV3 Keepalive

Chrome service workers die after 30s inactivity. The extension uses:
1. **Offscreen document** (`offscreen.html`) — maintains the WebSocket
2. **Ping every 25s** — keeps service worker alive
3. **Message relay** — `chrome.runtime.sendMessage` between offscreen and service worker

```javascript
// offscreen.js
const ws = new WebSocket('ws://localhost:8000/bridge?token=...');
setInterval(() => ws.send(JSON.stringify({type: 'ping'})), 25000);
```

## Android Reconnection

`BridgeClient.kt` uses exponential backoff:
- Initial delay: 3s
- Backoff: 2x each attempt
- Cap: 30s
- Reset on successful connection

```kotlin
private fun reconnectWithBackoff(attempt: Int = 0) {
    val delay = minOf(3000L * (2 shl attempt), 30000L)
    mainScope.launch {
        delay(delay)
        if (!isConnected()) connect()
    }
}
```

## Broker-Side (bridge_router.py)

- Token auth via `PCOS_BRIDGE_AUTH_TOKEN` env var
- Heartbeat check — disconnect clients that don't ping within 60s
- Client registry — track Chrome and Android clients separately
- Relay logic — forward messages between registered clients

## Key Files

- `broker/routers/bridge_router.py` — FastAPI WebSocket endpoint
- `broker/routers/_shared.py` — Shared bridge client state
- `apps/chrome-extension/background.js` — Service worker keepalive
- `apps/chrome-extension/offscreen.html` — Offscreen WS document
- `apps/android/app/src/main/java/com/pcos/edge/BridgeClient.kt` — Android WS client

## Testing

```bash
# Test WebSocket with wscat
wscat -c "ws://localhost:8000/bridge?token=your_token"
> {"type": "register", "platform": "chrome"}
> {"type": "ping"}
< {"type": "pong"}
```
