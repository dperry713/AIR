# AIR — Autonomous Software Engineering OS

AIR is a project to build a governed runtime for autonomous software engineering. It is intended to coordinate engineering tasks, enforce execution policy outside the model, isolate tool execution, preserve durable task history, and verify outcomes with inspectable evidence.

The project requirements and engineering constraints are defined in the [Master Engineering Contract](MEC.md).

## Current repository status

This repository currently contains the project contract and repository guardrails. It is not yet evidence that the full AIR runtime is implemented. Product features, builds, security controls, and runtime behavior must be reported as implemented only when they are present and independently verified.

## Repository verification

The [Repository Guardrails workflow](.github/workflows/ci.yml) runs on pull requests, pushes to main, and manual dispatch. At the current documentation-only stage, it tests and validates repository documentation using Python's standard library. It does not claim to build or test the AIR product.

See [CI Guardrails](docs/CI_GUARDRAILS.md) for the current checks, their scope, and the required GitHub branch-protection configuration.

## Project principles

- Security permissions are enforced by trusted runtime components, not by model assertions.
- Unknown or unauthorized operations fail closed.
- Execution, verification, and release status are supported by inspectable evidence.
- Human approval is explicit and auditable for actions that require it.
- CI must run real checks and propagate failures; unsupported checks must not be simulated or claimed.

## License

See [LICENSE](LICENSE).
