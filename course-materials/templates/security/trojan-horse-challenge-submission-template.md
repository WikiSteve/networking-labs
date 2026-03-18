# Trojan Horse Challenge Submission Template

- Filename: `Trojan Horse Challenge Submission Template.pptx`
- Subject: `security`
- Type: `submission-template`
- Reusable: `yes`
- Source file: [Source copy](../../sources/Trojan%20Horse%20Challenge%20Submission%20Template.pptx)
- Instructions: [Trojan Horse Challenge](../../challenges/security/trojan-horse-challenge.md)

## Summary

This reusable submission template defines the exact evidence package for the Trojan Horse challenge. It does not teach the attack or detection mechanics directly. Instead, it standardizes the four screenshots students must submit: browser proof of C2 reachability, terminal proof of the fake audit running, Python server log proof of the GET request and `200` status, and terminal proof of decoding the stolen base64 token. It functions as an assessment scaffold paired with the challenge document.

## Key Details

- The deck is explicitly framed as the submission template for the challenge.
- Screenshot 1 requires Windows browser proof showing `{"status":"received"}`.
- Screenshot 2 requires terminal proof of the audit finishing with "Audit Complete."
- Screenshot 3 requires Python log proof showing the GET request and `200` status.
- Screenshot 4 requires decode proof showing the recovered exfiltrated value.
- The file acts as a checklist and packaging guide for evidence rather than a lesson.
- The template is reusable across offerings because it defines a standard proof-of-completion structure.

## Tags

- `submission-template`
- `screenshots`
- `assessment-evidence`
- `trojan-horse`
- `challenge`
- `pptx`
