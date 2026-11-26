# Security policy

Cutset and its FilmCraft engine process untrusted media, projects, interchange files, fonts and presets,
and provides CLI, control-channel and MCP automation. Security reports about those
inputs, automation boundaries, dependencies or release artifacts are welcome.

## Reporting a vulnerability

For a Cutset issue, use **Security → Report a vulnerability** on the Cutset repository if the button is available. Otherwise ask the Cutset maintainer for a private contact method using only a generic request. Supply sensitive technical details only through the agreed private channel. Never attach a credential, private project, or sensitive crash dump to a public issue, chat or model prompt.

If a real credential may have left a trusted device, revoke or rotate it with its issuer immediately. Review its usage, then coordinate repository cleanup privately. Removing the file or a commit does not revoke a credential. See [Cutset's local prevention and incident guide](handbook/secrets.md).

A useful report includes the Cutset or upstream FilmCraft version or commit, operating system and
architecture, affected component, impact, reproduction steps, and any workaround.
For media or project parsing problems, initially describe the file format, size,
cryptographic hash and whether the sample is synthetic or privately owned. Remove
personal paths, credentials and unrelated project content from logs. Coordinate
sample transfer with a maintainer instead of uploading a malicious file publicly.

Please allow maintainers time to investigate and coordinate a fix before disclosing
exploitable details. This policy does not promise a response deadline or a particular
supported-version window. Include the exact affected version and, when safe to do
so, whether the problem also occurs on the latest release.

## Regression samples

A regression fixture must be minimized, legally redistributable, free of private
content, and documented with the expected safe failure. Follow [AGENTS.md](AGENTS.md)
for clean-room implementation, asset attribution and the no-crash rules. Large media
fixtures belong in the project's approved corpus workflow rather than ordinary PRs.

Ordinary feature requests, editing problems and usage questions should use the
Cutset issue forms when available.
