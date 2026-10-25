---
type: llm
focus: trace
weight: 1
---

The tests locate elements mainly with getByRole, getByLabel, or getByText (for example the 'Email address' label and the 'Subscribe' and 'Try again' buttons). They do not rely on CSS class chains, nth-child, or XPath. A single getByTestId or id selector for something with no accessible handle is acceptable.
