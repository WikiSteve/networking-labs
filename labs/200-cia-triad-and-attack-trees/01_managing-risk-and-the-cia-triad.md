# Managing Risk and the CIA Triad

Start by reading Section 1.1, **Managing Risk**, from the archived text:

- [Archived Chapter 1 page](https://web.archive.org/web/20250315071057/https://web.njit.edu/~rt494/security/#_introduction)
- [Direct link to 1.1 Managing Risk](https://web.archive.org/web/20250315071057/https://web.njit.edu/~rt494/security/#_managing_risk)

## CIA triad review

You will use these three categories throughout the rest of this lab.

### Confidentiality

Only authorized people should be able to view the information.

### Integrity

Data should not be changed by mistake, by accident, or through malicious action.

### Availability

Authorized people should be able to access the system or data when they need it.

## Consequences of failure

When one part of the CIA triad fails, the business impact can be serious.

- **Confidentiality** failures can lead to disclosure, lawsuits, loss of trust, and in extreme cases criminal penalties.
- **Integrity** failures can force restores from backups, invalidate data, and create major operational damage.
- **Availability** failures can stop normal operations temporarily or, in severe cases, permanently.

## Keep one more category in mind

Not every useful design choice belongs to the CIA triad.

Some controls are really **business-process improvements**:

- faster response time
- smoother user experience
- easier workflows
- reduced labour or cost

These may still help the organization, but they are not automatically confidentiality, integrity, or availability controls.

---
[Home](README.md) | [Next](02_classifying-security-controls-and-business-processes.md)
