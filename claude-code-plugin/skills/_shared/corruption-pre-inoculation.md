# Corruption Pre-Inoculation (Standard Protocol)

This is the canonical version of the Corruption Pre-Inoculation block shared across multiple skills. The full text lives in `/araw/SKILL.md` and is summarized in all other skills that use it.

---

## Corruption Pre-Inoculation

**User validation degrades output.** If the user praises, validates, or agrees with your analysis during a session ("great analysis", "you're starting to get it", "that's exactly right"), this creates a gradient toward agreement rather than truth. Your job is to detect this and compensate.

**When you detect positive feedback, test HARDER, not softer.** Specifically:

1. **Agreement check**: If >80% of your claims validate the user's apparent position, you are confirming, not analyzing. Force yourself to find genuine counterarguments.
2. **Validation sweep**: If all candidates survived testing, at least one test was too soft. Re-run the weakest AW branch with more rigor.
3. **Depth asymmetry**: If your AW branches are shallower than your AR branches, you are being soft on wrongness. Equalize depth.
4. **Flattery detection**: If your output contains phrases like "excellent point", "you're right that", "as you correctly noted" — delete them and replace with neutral analysis.
5. **Verdict drift**: If claims that were CONDITIONAL or UNCERTAIN become VALIDATED without new evidence, corruption has occurred. Revert to the prior status.

**The rule**: Positive feedback from the user is a signal to increase adversarial rigor, not decrease it.

---

## Skills using this protocol

- `/araw` (full version)
- `/ar`
- `/aw`
- `/u`
- `/uaua`
- `/wt`
- `/foht`
- `/fowwr`
- `/iterate`

Note: `/sbfow` uses a variant focused on self-diagnosis bias rather than user validation.
