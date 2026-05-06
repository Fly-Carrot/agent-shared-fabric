# Security Model

## Never Publish

Do not publish:

- `memory/*.ndjson`
- `sync/*.ndjson`
- `archive/`
- private project overlays
- raw user prompts by default
- API keys or `.env` files
- runtime private databases
- browser profiles
- cookies
- workspaceStorage
- Antigravity `.pb` state

## Generated Mirrors Are Not Canonical

Files under runtime-owned locations such as `~/.gemini` or `~/.codex` may be generated mirrors.

They are runtime adapters, not the source of truth.

## Secret Handling

Use environment variables at runtime.

Example:

```text
CONTEXT7_SECRET
ZOTERO_API_KEY
ZOTERO_LIBRARY_ID
```

Do not put concrete values in registries.
