# Using ReasoningTool as a ChatGPT skills plugin

This repository includes a ChatGPT/Codex plugin manifest at:

```text
.codex-plugin/plugin.json
```

The manifest exposes the existing skill library under:

```text
claude-code-plugin/skills/
```

## Install in ChatGPT

1. Connect the GitHub account that can access this repository.
2. Open **Plugins → Skills** in ChatGPT.
3. Add or import the `benjam3n/reasoningtool` repository.
4. Select the `main` branch after this change is merged.

ChatGPT should discover `.codex-plugin/plugin.json` and load the skill folders referenced by its `skills` field.

## Usage

Invoke a specific skill by name, or ask ReasoningTool to route the request. Examples:

```text
Use the claim skill to test: <claim>
Use ReasoningTool to decide between <option A> and <option B>
Analyze this problem with the best matching ReasoningTool skill
```

## Notes

- The repository remains the source of truth; updating the repository updates what is available after the plugin refreshes.
- Some skills were originally written with Claude-style placeholders such as `$ARGUMENTS`. ChatGPT generally receives the current user request in context, but any skill that depends on literal placeholder substitution may need a later compatibility pass.
