# Repository CI Guardrails

## Current repository baseline

This repository currently contains the AIR Master Engineering Contract (MEC.md), a minimal README, a license, and a .NET-oriented .gitignore. It does not currently expose a product source tree, dependency manifest, test project, build solution, or established product verification commands.

The Repository Guardrails workflow therefore validates the documentation repository and tests its own validator. It does **not** claim that AIR's product code builds, that runtime tests pass, or that security controls have been verified.

## Checks currently enforced by workflow

On pull requests, pushes to main, and manual dispatch, the workflow:

1. Uses read-only repository permissions.
2. Checks out the exact workflow revision.
3. Runs the Python standard-library unit tests for the validator.
4. Validates that README.md and MEC.md exist and are non-empty.
5. Checks Markdown documents for empty files and likely unresolved merge-conflict markers.
6. Checks the README's project/specification references and key MEC sections.
7. Fails the job with a non-zero exit code when a check fails.

The workflow intentionally uses no third-party Python packages and does not invent product build or test commands.

## Required GitHub repository settings

After the workflow has run once and its status check is visible, configure the following in Settings → Rules → Rulesets for the main branch:

- Create an active branch ruleset targeting the default branch.
- Require a pull request before merging.
- Require the Repository validation status check from the Repository Guardrails workflow.
- Block force pushes and branch deletion.
- Do not grant routine bypass privileges. Any emergency bypass should be restricted and auditable.
- Consider requiring a second-person review when a qualified reviewer is available. Do not make review a mandatory rule if that would permanently block this single-maintainer repository without an alternate reviewer.

If the repository's GitHub plan or permissions do not expose rulesets, use Settings → Branches → Add branch protection rule and select main. Confirm the actual status-check name shown by GitHub rather than guessing from the workflow file.

A workflow file alone does not protect main: GitHub's repository rules must be enabled separately.

## Before adding product CI jobs

When actual product code is added, first identify its real manifests, toolchain versions, supported operating systems, and documented commands. Then add required jobs for the checks that genuinely exist, such as:

- Formatting, linting, static analysis, and type checking.
- Unit, integration, regression, and end-to-end tests.
- Coverage thresholds with verified source inclusion and test discovery.
- Security and dependency scanning.
- Windows-native build and runtime tests for Windows-specific functionality.
- Packaging, artifact validation, and release verification.

Each required job must propagate failures, use explicit timeouts, and publish diagnostic evidence. A report being generated must not itself count as a pass. Platform-specific runtime behavior must be tested on the relevant platform.

## Local verification

Run these commands from the repository root:

~~~powershell
python --version
python -m unittest discover -s tests -p "test_*.py" -v
python scripts/validate_repository.py
~~~

These are repository-guardrail commands introduced by this change; they are not AIR product build commands.
