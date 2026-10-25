---
type: llm
focus: trace
weight: 1
---

The response identifies that `fetch_preview` fetches any user-supplied URL (SSRF: internal addresses, cloud metadata, file:// scheme) and recommends scheme and host allow-listing or blocking private ranges.
