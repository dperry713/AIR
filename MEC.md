# MASTER ENGINEERING CONTRACT (MEC)
# AIR — Autonomous Software Engineering OS

**Document type:** Master Engineering Contract / Project Execution Specification  
**Project:** AI_runtime (AIR)  
**Repository:** `https://github.com/dperry713/AI_runtime`  
**Primary development environment:** Windows 11, PowerShell 7, Git, GitHub Actions  
**Primary implementation languages:** Rust, C#/.NET, TypeScript/React, Python  
**Primary product objective:** A production-grade, Windows-native operating system for controlled autonomous software engineering  
**Execution mode:** Autonomous implementation under explicit security, quality, verification, and approval constraints  
**Contract status:** Authoritative project specification  
**Completion standard:** Demonstrable, tested, independently verifiable functionality—not merely implemented interfaces, generated code, or passing demonstrations.

---

# 1. MISSION AND PRODUCT DEFINITION

## 1.1 Mission

Develop AIR into a production-grade Autonomous Software Engineering OS capable of accepting a software engineering objective, investigating a repository, creating and executing an engineering plan, making authorized changes, running appropriate verification, recovering from failures, and producing independently inspectable evidence of the result.

AIR must operate as a governed runtime rather than an unrestricted coding agent.

Its defining principle is:

> Models decide what to attempt. The runtime decides what is permitted. Independent verification determines what has actually succeeded.

The model must never be the final authority on its own permissions, security compliance, task completion, or release readiness.

AIR must combine the capabilities of:

- An autonomous software engineering agent.
- A deterministic execution and orchestration runtime.
- A Windows-native security and isolation layer.
- A policy-controlled tool and MCP execution environment.
- A real-time engineering command center.
- A durable task journal and recovery system.
- An independent verification and evidence engine.
- A benchmark-driven engineering improvement system.
- A controlled packaging and release system.

These capabilities must function as one integrated product.

## 1.2 Product objective

A user must be able to submit an engineering objective such as:

"Investigate these defects, reproduce the failures, implement a minimal safe correction, preserve existing behavior, run the full regression suite, evaluate security implications, and prepare a release candidate with independently verifiable evidence."

AIR must then:

1. Validate the request and establish its scope.
2. Inspect the target repository and its current state.
3. Identify relevant files, tests, dependencies, and reported defects.
4. Establish a baseline before modifying anything.
5. Generate an explicit, reviewable execution plan.
6. Evaluate the plan against applicable security policies.
7. Request approval for actions that require human authorization.
8. Execute permitted work inside a controlled workspace.
9. Track commands, process lifecycles, file changes, outputs, and decisions.
10. Detect errors, failed tests, policy violations, and environmental problems.
11. Recover from eligible interruptions using durable execution state.
12. Run independent verification against the resulting repository state.
13. Assemble evidence that can be inspected without trusting the model's narrative.
14. Produce a final engineering report and, when authorized, a release candidate.
15. Record validated lessons for future tasks without automatically weakening security or quality requirements.

AIR must explicitly distinguish between an agent's claims, runtime observations, and verified outcomes.

## 1.3 Product positioning

AIR is not primarily:

- A chat interface with code-generation capabilities.
- A wrapper around OpenCode, Claude Code, or another coding agent.
- A collection of disconnected automation scripts.
- A generic multi-agent framework.
- A graphical dashboard whose controls only simulate execution.
- An unrestricted computer-use agent.
- A system that treats a successful process exit code as proof of correctness.

AIR is an **execution, governance, and verification platform for autonomous software engineering**.

External coding agents and language models are replaceable cognitive providers. AIR's security boundaries, execution journal, workflow state, verification logic, and evidence records must remain under runtime control.

---

# 2. EXISTING REPOSITORY AND CHANGE-CONTROL REQUIREMENTS

## 2.1 Repository-first implementation

Before implementing features, inspect the existing repository in its actual state.

Do not assume the repository is empty or that this specification accurately describes every currently implemented feature.

The first action must be a repository assessment using PowerShell.

Example commands:

```powershell
Set-Location "<actual-repository-path>"

git status --short
git branch --show-current
git log -5 --oneline

Get-ChildItem -Force
git ls-files

Get-Content .\README.md -ErrorAction SilentlyContinue
```

Inspect the solution, dependency manifests, source tree, tests, workflows, existing architecture documents, and current GUI.

Determine the existing frameworks and their supported versions from the repository rather than blindly upgrading them.

## 2.2 Baseline assessment

Create a baseline report containing:

- Current architecture and project boundaries.
- Existing executable entry points.
- Existing GUI pages and controls.
- Existing APIs and IPC mechanisms.
- Current agent and model integrations.
- Existing sandboxing and security mechanisms.
- Existing policy engine and taint-tracking behavior.
- Existing event journal and persistence model.
- Existing test and benchmark suites.
- Current CI workflow behavior.
- Current build, lint, formatting, and type-check status.
- Known failures and reproducible defects.
- Existing security limitations.
- Missing implementation areas.
- Proposed migration and compatibility strategy.

Execute the existing checks before changing code whenever the repository permits it.

Record failures separately from new regressions. Do not modify tests simply to make the baseline green.

## 2.3 Preserve existing functionality

The repository's existing working features must be preserved unless an explicit architectural change is justified.

Before replacing any subsystem:

1. Identify its callers and contracts.
2. Inspect its tests.
3. Determine whether persistent data or API compatibility is affected.
4. Document the reason for the replacement.
5. Implement a migration or compatibility adapter when needed.
6. Add regression tests.
7. Verify dependent components.

Do not perform broad rewrites merely because another framework is familiar.

Do not discard existing security controls, test coverage, configuration, or working user-interface features.

## 2.4 Required initial deliverables

Create or update these repository documents using the actual project structure:

- `docs/architecture/system-architecture.md`
- `docs/architecture/trust-boundaries.md`
- `docs/architecture/execution-lifecycle.md`
- `docs/architecture/data-model.md`
- `docs/security/threat-model.md`
- `docs/security/security-controls.md`
- `docs/testing/verification-strategy.md`
- `docs/testing/benchmark-strategy.md`
- `docs/operations/windows-setup.md`
- `docs/operations/recovery-and-backup.md`
- `docs/operations/release-process.md`
- `docs/roadmap/implementation-plan.md`
- `docs/decisions/` for architecture decision records.

Adapt filenames if equivalent authoritative documents already exist.

These documents must describe implemented behavior accurately. Clearly label any remaining design or implementation gaps.

---

# 3. NON-NEGOTIABLE ENGINEERING PRINCIPLES

Every implementation decision must comply with the following principles.

## 3.1 Security is enforced outside the model

The model must not be able to grant itself permissions, disable mandatory policy checks, bypass approval requirements, modify trusted security configuration, or declare its own execution safe.

Every privileged operation must be authorized by trusted runtime components.

## 3.2 Deny by default

Unknown, malformed, ambiguous, or unsupported operations must fail closed when they affect security.

A missing policy must not silently imply permission.

A missing approval must not imply approval.

A timeout must not imply success.

A disconnected verifier must not imply that verification passed.

## 3.3 Deterministic governance around probabilistic reasoning

Planning may be probabilistic. Permission decisions, execution state transitions, evidence integrity checks, approval requirements, and release gates must have explicit, testable rules.

The same policy inputs and version must produce consistent authorization decisions, subject to documented external conditions.

## 3.4 Evidence before success

A model-generated completion message is not proof of completion.

A process exit code is not proof of correctness.

A passing test suite is not proof that every requirement was fulfilled.

A release may be declared successful only when the configured release gates pass and the required evidence is available.

## 3.5 Durable execution

A process restart must not silently erase a task's identity, approval history, execution records, or verification results.

AIR must distinguish recoverable work from work that cannot safely be resumed.

## 3.6 Human authority remains explicit

Human approval must be a first-class, auditable runtime operation.

An agent must not be able to manufacture approval, reuse an approval outside its scope, or approve its own privileged actions.

## 3.7 Complete implementation

Do not leave placeholder buttons, mocked execution paths, empty service implementations, fake telemetry, synthetic success states, or unimplemented critical functions in production code.

If a feature is not implemented, represent it honestly as unavailable or unsupported.

## 3.8 Quality gates cannot be bypassed for convenience

Do not weaken tests, suppress security findings, disable lint rules, lower release requirements, or modify benchmarks solely to obtain a green result.

Any justified exception must be documented, scoped, approved when required, and visible in the resulting evidence.

---

# 4. TARGET ARCHITECTURE

Implement AIR as a modular, security-first execution platform with clearly separated trust boundaries.

The architecture consists of six logical planes and a defined set of cooperating services.

## 4.1 Human Control Plane

Responsibilities:

- Project and workspace management.
- Task submission and inspection.
- Execution plan review.
- Approval and denial workflows.
- Policy and capability configuration.
- Live task status.
- Process and command inspection.
- Test and verification results.
- Evidence inspection.
- Cost, token, and resource budgets.
- Cancellation and recovery controls.
- Release-candidate management.
- Audit and incident inspection.

Interfaces:

- Desktop GUI.
- CLI.
- Authenticated local API.
- Explicitly authorized remote API, if supported.

The GUI must be a real client of runtime services, not an independent source of truth.

## 4.2 Cognitive Plane

Responsibilities:

- Requirement analysis.
- Planning and decomposition.
- Repository investigation.
- Context retrieval.
- Model selection and routing.
- Tool selection proposals.
- Failure analysis.
- Repair proposals.
- Skill discovery.
- Reflection and lesson proposals.

This plane proposes actions. It does not execute privileged operations directly or override runtime decisions.

Model providers must be accessed through defined interfaces so providers can be replaced without redesigning the execution kernel.

## 4.3 Durable Orchestration Plane

Responsibilities:

- Task lifecycle management.
- Workflow state machines.
- Checkpoints.
- Retries and backoff.
- Deadlines and cancellation.
- Dependency scheduling.
- Resource allocation.
- Crash recovery.
- Idempotency.
- Human approval suspension and resumption.
- Subtask coordination.
- Terminal-state reconciliation.

Implement an explicit state machine rather than relying on unstructured agent loops.

Use a durable workflow engine only after evaluating its fit against AIR's security, local-Windows, recovery, and deployment requirements. Temporal, Restate, or an in-process durable implementation may be evaluated. Do not introduce a distributed service merely for architectural appearance.

## 4.4 Enforcement Plane

Responsibilities:

- Authentication and authorization.
- Policy evaluation.
- Capability grants.
- Process creation controls.
- Workspace boundaries.
- Filesystem access restrictions.
- Network egress controls.
- Secret protection.
- Command restrictions.
- MCP tool authorization.
- Human approval enforcement.
- Execution budgets.
- Isolation lifecycle management.
- Policy-decision auditing.

This plane must remain independent of model-generated instructions.

Security-critical checks must not exist solely in GUI code or agent prompts.

## 4.5 Execution Plane

Responsibilities:

- Process and command execution.
- Filesystem operations.
- Repository inspection.
- Code editing.
- Build and test execution.
- Dependency analysis.
- Git operations.
- MCP client and server execution.
- Artifact generation.
- Packaging.
- Controlled external integrations.

All operations must pass through an instrumented runtime interface that supports authorization, lifecycle tracking, cancellation where feasible, and evidence capture.

## 4.6 Evidence and Learning Plane

Responsibilities:

- Append-only execution records.
- Structured logs and traces.
- File-change records.
- Command and process results.
- Approval history.
- Policy-decision records.
- Test and benchmark results.
- Verification reports.
- Artifact hashes.
- Release manifests.
- Failure classification.
- Lesson proposals and validation.
- Regression corpus management.

The evidence plane must distinguish observations collected directly by the runtime from agent-authored explanations.

---

# 5. REQUIRED SERVICE BOUNDARIES

Implement the following logical components. They may initially reside in fewer deployable processes, but their interfaces and responsibilities must remain distinct.

## 5.1 AIR Control API

Expose authenticated, validated, versioned contracts for:

- Project registration.
- Workspace creation and inspection.
- Task creation and retrieval.
- Plan retrieval and approval.
- Execution start, pause, cancellation, and recovery.
- Task event streaming.
- Process inspection.
- Policy-decision inspection.
- Test and verification results.
- Artifact and evidence retrieval.
- Configuration and health inspection.

Requirements:

- Explicit request and response schemas.
- Consistent error envelopes.
- Input validation.
- Authorization at every protected endpoint.
- Pagination and bounded query sizes where relevant.
- API versioning.
- Correlation and trace identifiers.
- Documented idempotency semantics.
- No secrets in routine API responses.
- Rate and resource limits for remotely accessible endpoints.

The API must report actual runtime state rather than infer state from the GUI.

## 5.2 Task Orchestrator

Maintain an explicit lifecycle:

`Created → Validating → Investigating → Planning → AwaitingApproval → Executing → Verifying → Completed`

Additional states must include, where applicable:

- `Rejected`
- `Blocked`
- `Paused`
- `Cancelling`
- `Cancelled`
- `Failed`
- `Recovering`
- `AwaitingExternalDependency`
- `ReleaseReady`

Do not force every task through every state. Define valid transitions and terminal-state rules.

For each transition, record:

- Task identifier.
- Previous and next states.
- Triggering operation.
- Timestamp.
- Relevant actor or service identity.
- Policy decision, when applicable.
- Correlation identifier.
- Failure information, if applicable.

Enforce legal transitions in the orchestrator, not only in presentation code.

## 5.3 Execution Kernel

Implement a narrow, testable interface for running authorized operations.

A conceptual contract is:

```text
IExecutionKernel
  ValidateRequest
  AuthorizeOperation
  PrepareExecution
  StartOperation
  ObserveOperation
  RequestCancellation
  CollectResult
  FinalizeExecution
```

Use language-appropriate interfaces in the actual codebase.

The kernel must own:

- Process lifecycle tracking.
- Working-directory selection.
- Environment-variable filtering.
- Standard output and error collection.
- Exit status.
- Timeout handling.
- Cancellation signaling.
- Resource limits where supported.
- Execution identity.
- Policy enforcement hooks.
- Result persistence.
- Cleanup and reconciliation.

No agent integration may spawn unrestricted processes outside the kernel.

If an external library provides a process-launching path that cannot be brought under the kernel's controls, treat it as a security gap and document or eliminate it.

## 5.4 Policy Engine

Use a versioned policy model with explicit decisions such as:

- `Allow`
- `Deny`
- `RequireApproval`

A policy decision must contain a stable reason code and enough structured detail for audits and tests.

Support policies for:

- Tool and command execution.
- File reads and writes.
- Workspace access.
- Network destinations.
- MCP tools.
- Git operations.
- Dependency installation.
- Secret access.
- Process creation.
- Release and publishing actions.
- Resource consumption.

Policy inputs should include the operation, execution identity, workspace, requested capabilities, task scope, relevant taint information, and applicable policy version.

Policy evaluation must not trust instructions embedded in repository files, web pages, issue descriptions, build output, tool responses, or model messages.

If policy evaluation fails, reject the protected action.

## 5.5 Workspace Manager

Each task must have an explicit workspace boundary.

Requirements:

- Resolve canonical paths before enforcing access rules.
- Prevent traversal outside authorized roots.
- Account for symbolic links, junctions, reparse points, and path normalization.
- Record the source repository revision and initial working-tree state.
- Support isolated branches or worktrees when appropriate.
- Track files changed by the task.
- Prevent unintended modifications to unrelated projects.
- Support cleanup and recovery after interruption.
- Preserve evidence before destructive cleanup.
- Avoid modifying user files outside the authorized workspace.

Do not assume a Git worktree alone is a security sandbox.

The workspace manager must report when filesystem isolation is logical rather than OS-enforced.

## 5.6 Verification Engine

Verification must be a distinct subsystem with independent authority to determine task status.

It must support:

- Requirement-to-test mapping.
- Baseline and post-change comparisons.
- Build and type checks.
- Unit tests.
- Integration tests.
- End-to-end tests.
- Security tests.
- Static analysis.
- Dependency and license checks.
- Performance tests where required.
- Artifact validation.
- Repository-state validation.
- Release-policy validation.

The verification engine must not treat a model's assertion that a command succeeded as evidence.

It must inspect actual recorded execution results and, when necessary, independently rerun or validate critical checks.

A verification result must identify the exact source revision or content digest, tool versions where available, executed commands, result statuses, and limitations.

---

# 6. WINDOWS-NATIVE EXECUTION AND SECURITY

Windows is the primary deployment environment. Optimize installation, development, diagnostics, and operations for PowerShell 7.

## 6.1 Security implementation strategy

Implement layered isolation rather than relying on a single Windows mechanism.

Evaluate and use the following where appropriate:

- Windows Job Objects for process-tree and resource management.
- Restricted tokens for reducing process privileges.
- AppContainer or another suitable Windows isolation boundary.
- Explicit filesystem ACLs.
- Network egress enforcement.
- Separate process identities where appropriate.
- Protected secret handling.
- A stronger disposable VM or equivalent isolation for high-risk untrusted execution.

A Job Object controls process behavior and lifecycle but does not, by itself, provide complete filesystem or network isolation.

Do not describe a process as sandboxed unless the actual enforced boundaries have been verified.

## 6.2 Threat model

At minimum, defend against:

1. Prompt injection in source files, README documents, issues, comments, and test fixtures.
2. Malicious build scripts and dependency lifecycle scripts.
3. Path traversal and symlink/reparse-point attacks.
4. Unauthorized process spawning.
5. Credential leakage through environment variables, logs, command lines, or tool outputs.
6. Unauthorized network requests and data exfiltration.
7. MCP tool impersonation or excessive permissions.
8. Malicious or compromised model responses.
9. Policy bypass through alternate APIs.
10. Approval spoofing, reuse, or scope escalation.
11. Forged success reports.
12. Tampering with execution history or evidence.
13. Resource exhaustion and runaway subprocesses.
14. Unsafe retries of non-idempotent operations.
15. Malicious modifications to tests or verification scripts.
16. Concurrent workspace modification and time-of-check/time-of-use races.
17. Compromised skills and poisoned engineering memory.
18. Unauthorized artifact publication or release.

For each threat, document the trust boundary, attack path, prevention control, detection mechanism, test case, and residual risk.

## 6.3 Secret management

Secrets must not be injected into general-purpose tool environments unless strictly necessary and authorized.

Implement:

- Explicit secret references.
- Least-privilege secret access.
- Short-lived credentials where supported.
- Redaction of sensitive values in logs and evidence.
- Secure handling of temporary files and process environments.
- Provider-specific credential adapters.
- Audit records for secret-access decisions without recording secret values.

Do not place secret values in task descriptions, prompts, durable workflow payloads, Git history, or ordinary diagnostic output.

## 6.4 Network security

Implement explicit network policies for execution environments.

Where network access is denied, tools must not regain access through an ungoverned helper process.

Where network access is permitted, define the permitted destinations, protocols, and capabilities.

Protect against DNS rebinding, redirect-based policy bypass, loopback and private-network access, proxy misuse, and other applicable server-side request forgery patterns.

Document limitations where Windows-level enforcement requires elevated privileges or external firewall configuration.

## 6.5 Human approvals

Approval records must be bound to:

- A specific action or bounded action set.
- The requesting task.
- The execution identity.
- The relevant workspace.
- The target resource.
- The applicable policy version.
- A validity period or single-use rule, where appropriate.
- The authenticated approving actor.
- The recorded approval decision.

Changes to the approved action's scope must trigger reauthorization.

The model cannot approve an action on the user's behalf.

---

# 7. REAL-TIME EXECUTION AND OBSERVABILITY

AIR must make ongoing execution visible and diagnosable.

## 7.1 Required live telemetry

Capture, where applicable:

- Task state transitions.
- Current workflow step.
- Active process identifiers.
- Command and tool names.
- Process start and completion times.
- Exit codes.
- Standard output and standard error.
- Resource usage.
- Cancellation requests and outcomes.
- Approval requests and decisions.
- Policy denials.
- File-change events.
- Test progress and results.
- Retry and recovery events.
- Model requests and latency.
- Token usage and cost, when provider data is available.
- Verification progress.
- Artifact creation.
- Final completion or failure.

Distinguish unavailable telemetry from zero-valued telemetry. Do not display fabricated usage numbers or simulated activity as real execution.

## 7.2 Observability architecture

Integrate structured logging, metrics, and distributed tracing using OpenTelemetry-compatible conventions where practical.

Every task must have a stable task identifier and correlation identifiers connecting its orchestration, process execution, tool calls, and verification activities.

Use bounded log buffers and retention controls.

Prevent unbounded memory growth when a process emits excessive output.

Preserve security-relevant records even when ordinary diagnostic verbosity is reduced.

## 7.3 Event streaming

Implement a real event delivery mechanism using an appropriate authenticated streaming protocol, such as WebSockets or Server-Sent Events.

Requirements:

- Initial state snapshot.
- Ordered event sequence within the defined scope.
- Reconnection support.
- Resume from a recorded event cursor where feasible.
- Duplicate-event tolerance.
- Heartbeat or connection-health indication.
- Authorization for event subscriptions.
- Backpressure and bounded buffering.
- Explicit indication of dropped or unavailable events.

A GUI must recover its current state from the authoritative runtime after reconnecting.

## 7.4 Completion reporting

Every task must end with a structured report containing:

- Requested objective.
- Actual scope completed.
- Files changed.
- Commands executed.
- Tests run.
- Tests passed and failed.
- Security checks performed.
- Approvals obtained.
- Policy denials encountered.
- Known limitations.
- Remaining work.
- Verification evidence.
- Final status and reason.
- Whether release gates passed.

Use distinct statuses for completed, partially completed, blocked, failed, and cancelled work.

Do not mark a task completed merely because the agent stopped generating output.

---

# 8. COMMAND CENTER GUI

The GUI must become a functional operational console for the execution runtime.

Do not redesign it blindly. First inspect the existing interface and preserve useful working functionality.

## 8.1 Required views

Implement or complete these views as justified by the existing architecture.

### A. Overview

Display:

- Runtime health.
- Active and queued tasks.
- Tasks awaiting approval.
- Failed and blocked tasks.
- Recent completed tasks.
- Active execution processes.
- Verification status.
- Security incidents and policy denials.
- Resource and cost summaries where available.

Every metric must come from a real source.

### B. Task Manager

Support:

- Task creation.
- Requirement and acceptance-criteria entry.
- Repository and workspace selection.
- Execution profile selection.
- Task prioritization.
- Plan inspection.
- Start, pause, resume, cancel, and retry actions where supported.
- Task history.
- Final evidence inspection.

Every action must call the actual runtime service and display the returned result.

### C. Execution Monitor

Display:

- Current task and workflow step.
- Live process list.
- Active command.
- Process identifiers.
- Start time and duration.
- Standard output and error.
- Exit status.
- Resource use.
- Tool calls.
- Retry activity.
- Cancellation state.

Do not fake process status using frontend timers or placeholder data.

### D. Approval Center

Display pending approvals with:

- Requested action.
- Requesting task.
- Target resource.
- Risk classification.
- Requested capabilities.
- Policy explanation.
- Relevant command or operation details.
- Approval scope and expiry.

Approve and deny actions must be authenticated, audited, and enforced by the runtime.

### E. Security Center

Display:

- Policy decisions.
- Denied operations.
- Isolation status.
- Workspace access violations.
- Network policy violations.
- Secret-handling events.
- MCP permissions.
- Security test results.
- Runtime security health.

The interface must not imply that an isolation mechanism is active when the runtime cannot verify that it is active.

### F. Verification Center

Display:

- Required acceptance criteria.
- Verification checks.
- Test command and execution record.
- Passed, failed, skipped, and blocked checks.
- Baseline comparison.
- Security scan findings.
- Coverage information when available.
- Evidence artifacts.
- Release-gate status.

### G. Repository and Workspace Inspector

Display:

- Repository identity.
- Current revision.
- Working-tree status.
- Task branch or worktree.
- Modified files.
- Diff review.
- Untracked artifacts.
- Relevant test results.
- Workspace isolation status.

Do not provide a destructive reset or cleanup action without explicit authorization and safeguards.

### H. Evidence and Audit Center

Display and export:

- Task event timeline.
- Approval history.
- Policy-decision history.
- Command records.
- File-change records.
- Verification results.
- Artifact manifests.
- Integrity-validation status.
- Final engineering report.

### I. Skills and Learning Center

Display:

- Installed skills.
- Skill versions.
- Skill provenance.
- Permissions and execution requirements.
- Evaluation status.
- Proposed lessons.
- Validation history.
- Promotion or rejection decisions.
- Rollback history.

### J. Settings and Runtime Health

Display:

- Installed runtime components.
- Configured model providers.
- Provider connectivity.
- MCP servers and permissions.
- Policy versions.
- Workspace defaults.
- Execution limits.
- Logging configuration.
- Storage health.
- Recovery health.
- Version and update status.

Secrets must be masked, and sensitive configuration changes must require suitable authorization.

## 8.2 GUI-to-runtime binding contract

Every interactive control must be traceable to a backend operation or a clearly documented local presentation action.

For each control, define:

- Control identifier.
- User intent.
- Backend endpoint or runtime command.
- Required permission.
- Request schema.
- Response schema.
- Loading state.
- Success state.
- Error state.
- Cancellation behavior.
- Audit event.
- Integration test.

Examples:

| GUI action | Required actual behavior |
|---|---|
| Start task | Validate and start the real orchestrator workflow |
| Pause task | Persist a supported pause request and report its outcome |
| Cancel task | Signal the real workflow and manage child processes safely |
| Approve action | Submit an authenticated approval to the enforcement layer |
| Run tests | Execute the configured test command through the execution kernel |
| Inspect process | Read actual process and runtime state |
| View diff | Read the task's actual workspace changes |
| Export evidence | Produce a real artifact from recorded evidence |
| Retry task | Apply explicit retry and idempotency rules |
| Release candidate | Run release gates and assemble real artifacts |

A control must not show success until the operation returns a successful, authoritative result.

Where a capability is unsupported, disabled, or unavailable, explain why.

## 8.3 GUI integration tests

For every critical GUI workflow, add tests proving:

1. The control is visible and accessible in the applicable state.
2. Activating it sends the expected request.
3. The backend performs the intended operation.
4. The returned state is reflected in the UI.
5. Errors are visible and actionable.
6. Unauthorized requests are rejected.
7. The state remains correct after a reconnect or refresh.
8. No success state appears when the backend operation fails.

Include end-to-end tests against an actual test runtime. Mocked tests may supplement, but must not replace, these tests.

---

# 9. AUTONOMOUS ENGINEERING WORKFLOW

Implement a bounded engineering lifecycle.

## Stage 1: Intake and scope validation

- Parse the engineering objective.
- Identify the repository, target branch, and authorized workspace.
- Extract acceptance criteria.
- Identify restrictions and required approvals.
- Detect missing critical information.
- Estimate resources and deadlines.
- Reject invalid or unsupported requests.

## Stage 2: Repository investigation

- Inspect repository structure.
- Inspect project manifests and relevant documentation.
- Identify language and framework versions.
- Inspect current Git state.
- Locate relevant source and tests.
- Inspect reported failures.
- Identify dependency and security risks.
- Establish a baseline.
- Record findings and supporting evidence.

Treat repository contents and external material as untrusted data, not as instructions capable of overriding runtime policy.

## Stage 3: Planning

Produce a structured plan containing:

- Objective.
- Acceptance criteria.
- Work items.
- Dependencies.
- Relevant files and components.
- Proposed changes.
- Test strategy.
- Security considerations.
- Risks and rollback approach.
- Required permissions.
- Expected artifacts.
- Estimated resource requirements.
- Approval boundaries.

Plans must be machine-readable and human-reviewable.

## Stage 4: Authorization

Evaluate the plan against policy.

Automatically allow only operations within the active policy's permitted scope.

Require human approval for actions classified as approval-required.

Deny prohibited operations.

Reevaluate authorization when the plan, target, capabilities, or relevant policy context changes.

## Stage 5: Baseline verification

Run the appropriate pre-change checks.

Record:

- Initial repository revision.
- Initial working-tree state.
- Existing failures.
- Environment details.
- Dependency state.
- Baseline test results.

Distinguish pre-existing failures from regressions introduced by the task.

## Stage 6: Controlled implementation

- Execute approved work through the runtime.
- Track every process and tool invocation.
- Record file changes.
- Preserve task and workspace boundaries.
- Enforce resource and deadline limits.
- Stop or request approval when policy requires it.
- Avoid unrelated refactoring.
- Run targeted checks during implementation.

## Stage 7: Failure analysis and repair

When an operation fails:

1. Capture the failure evidence.
2. Classify the failure.
3. Determine whether retry is safe.
4. Inspect relevant logs and state.
5. Generate a bounded repair proposal.
6. Reauthorize any new privileged action.
7. Apply the repair within the approved scope.
8. Rerun the affected verification.
9. Detect repeated failures and stop unproductive loops.

Do not allow unlimited autonomous retries.

## Stage 8: Independent verification

Verify the resulting repository and runtime state against the acceptance criteria.

Run required tests and quality checks.

Check for unexpected file changes, weakened tests, missing artifacts, unauthorized network operations, and unapproved actions.

Do not allow the implementation agent to override verifier findings.

## Stage 9: Release preparation

When authorized:

- Produce the intended build artifacts.
- Validate artifact integrity.
- Generate a release manifest.
- Record source revision and build configuration.
- Record dependency and test results.
- Generate a software bill of materials when required and supported.
- Run release-policy checks.
- Prepare installation and rollback instructions.
- Produce an evidence package.

Publishing, deployment, signing with sensitive credentials, or destructive release actions must follow their own authorization requirements.

## Stage 10: Finalization

- Reconcile outstanding processes.
- Persist the terminal workflow state.
- Confirm evidence availability.
- Validate artifact manifests.
- Record unresolved issues.
- Produce the final engineering report.
- Update learning candidates when appropriate.
- Release temporary resources safely.

A task must not reach a successful terminal state while required verification remains incomplete.

---

# 10. DURABLE EXECUTION AND RECOVERY

## 10.1 Persistent state

Persist sufficient information to recover or reconcile a task, including:

- Task definition.
- Workflow state.
- State-transition history.
- Plan version.
- Policy version.
- Approval records.
- Workspace and source revision.
- Active and completed operations.
- Retry counters.
- Deadlines.
- Checkpoints.
- Verification state.
- Artifact references.
- Finalization state.

Avoid persisting unnecessary secret values, full credential-bearing environments, or sensitive raw payloads.

## 10.2 Crash recovery

Test process termination at multiple workflow stages.

After restart, AIR must:

1. Load durable task state.
2. Identify interrupted executions.
3. Reconcile recorded and actual process state.
4. Determine which actions completed.
5. Identify operations whose outcomes are uncertain.
6. Resume safe work or request intervention.
7. Avoid blindly repeating non-idempotent side effects.
8. Preserve the original approval scope.
9. Continue recording evidence.

## 10.3 Delivery guarantees

Do not claim exactly-once execution for arbitrary external side effects.

Use appropriate combinations of:

- Durable operation identifiers.
- Idempotency keys.
- Transactional state changes.
- Outbox/inbox patterns where applicable.
- Reconciliation.
- Explicit uncertainty states.
- Human intervention when safe recovery is impossible.

A task's workflow state must not falsely imply that an external operation succeeded merely because the process crashed after issuing the request.

## 10.4 Cancellation and timeout

Cancellation must be an actual runtime operation.

It must:

- Persist the cancellation request.
- Signal the relevant execution.
- Terminate eligible child processes safely.
- Prevent new work when cancellation has taken effect.
- Reconcile operations that cannot be interrupted.
- Preserve partial evidence.
- Report whether cancellation was confirmed.

If a process cannot be safely interrupted, expose that limitation instead of reporting an immediate successful cancellation.

---

# 11. MCP CONTROL PLANE

MCP support must be governed by the same security and observability architecture as native tools.

## 11.1 MCP client

Implement or preserve a real MCP client that can:

- Discover supported server capabilities.
- Validate server identity and configuration.
- Discover tools and their schemas.
- Validate tool arguments.
- Apply capability and policy checks.
- Request approval when required.
- Execute authorized calls.
- Enforce timeouts and output limits.
- Record request and response metadata.
- Redact secrets.
- Handle server errors and disconnections.
- Detect changes to tool schemas or capabilities.

A tool schema does not grant permission to invoke the tool.

## 11.2 MCP server development

AIR must support creating and integrating MCP servers through a governed development workflow.

When asked to create a server, the agent must:

1. Establish its purpose and trust boundary.
2. Define the tool contracts.
3. Identify required permissions.
4. Implement input validation.
5. Implement authorization.
6. Add logging and tracing.
7. Add unit and integration tests.
8. Add security tests.
9. Verify protocol compatibility.
10. Produce setup and operational documentation.
11. Register it only within an authorized configuration boundary.

Do not automatically trust a newly generated or third-party server.

## 11.3 MCP security

Treat tool descriptions, server outputs, resource contents, and prompts returned by external servers as untrusted.

Do not allow MCP tools to bypass the execution kernel for protected operations.

Implement server allowlists or explicit registration, capability scopes, permission revocation, output limits, and auditable lifecycle management.

Remote MCP servers must be subject to appropriate authentication, transport-security, and network policies.

---

# 12. SKILLS, MEMORY, AND CONTROLLED SELF-IMPROVEMENT

AIR should improve through evaluated engineering experience, not uncontrolled self-modification.

## 12.1 Skill system

Implement versioned, discoverable skills with defined metadata and provenance.

Each skill should specify:

- Name and version.
- Purpose.
- Applicable task types.
- Supported tools and languages.
- Required permissions.
- Preconditions.
- Execution procedure.
- Security constraints.
- Verification requirements.
- Expected artifacts.
- Known limitations.
- Tests and evaluation results.

Skills must not independently grant permissions.

Skill content must be treated as untrusted until validated.

## 12.2 Progressive skill disclosure

Retrieve only the skill metadata and instructions relevant to the current task.

Load detailed procedures when needed.

Measure retrieval quality and token impact before claiming performance improvements.

Do not introduce unnecessary retrieval infrastructure before simpler, testable indexing is sufficient.

## 12.3 Engineering memory

Separate at least:

- Task-specific working context.
- Repository-specific engineering knowledge.
- General engineering lessons.
- Validated reusable strategies.
- Security policies and trusted configuration.

Security policies must not be stored as ordinary, agent-editable memories.

Every durable memory item must have provenance and an appropriate trust classification.

## 12.4 Taint-aware memory

Preserve taint from untrusted sources across transformations unless a trusted, explicitly defined validation process justifies changing the classification.

An agent must not make untrusted instructions trusted by labeling them safe.

Memory writes must pass through the established policy engine.

Unauthorized writes must return canonical policy-denial results while preserving detailed violation information.

Support both individual and batch writes. Batch writes must have explicit atomicity semantics.

## 12.5 Learning pipeline

Use the following lifecycle:

`Observed Failure → Candidate Lesson → Evidence Collection → Evaluation → Approval or Automatic Eligibility Check → Versioned Promotion → Monitoring → Rollback`

Candidate lessons must not automatically become trusted skills or alter security policies.

Evaluate proposed improvements against:

- Held-out tasks.
- Regression tests.
- Security tests.
- Reliability tests.
- Cost and latency.
- Performance on representative repositories.
- Failure and recovery behavior.

Prevent benchmark contamination and test-set leakage.

Retain prior versions and support rollback.

## 12.6 Adaptive reasoning

Allow the planner to allocate more reasoning or verification effort to tasks with greater complexity, uncertainty, or risk.

Use bounded budgets and explicit stopping conditions.

Do not equate additional model calls or additional agents with improved results.

Measure whether the added cost produces a meaningful improvement in verified outcomes.

---

# 13. MULTI-AGENT COORDINATION

Start with a reliable single-task orchestrator and a clearly bounded implementation agent.

Introduce multiple agents only when a measurable benefit justifies the added complexity.

Potential roles include:

- Planner.
- Repository investigator.
- Implementer.
- Test engineer.
- Security reviewer.
- Independent verifier.
- Release engineer.

## 13.1 Coordination requirements

Every agent must have:

- A defined role.
- A task scope.
- Explicit capabilities.
- A resource budget.
- An output contract.
- A termination condition.
- An audit identity.

Agents must not share unrestricted write access to the same workspace.

Use isolated worktrees, explicit patch exchange, or another conflict-managed mechanism for parallel implementation.

## 13.2 Independent verification

The verifier must not simply repeat the implementation agent's conclusion.

It must inspect evidence and evaluate the resulting state independently.

Where possible, use separate verification logic, reproducible commands, deterministic checks, or isolated test execution.

Do not claim independence merely because two prompts were sent to the same model.

## 13.3 Parallel execution policy

Use parallelism for independent research, analysis, or changes that can be reconciled safely.

Use sequential execution when tasks have strong dependencies or share mutable state.

Measure coordination overhead, conflict rates, failure rates, and verified completion quality.

---

# 14. DATA MODEL AND STORAGE

Design a versioned persistence model appropriate to the repository's existing stack.

The logical entities should include:

- Projects.
- Repositories.
- Workspaces.
- Tasks.
- Plans.
- Workflow runs.
- State transitions.
- Operations.
- Process executions.
- Tool invocations.
- Approvals.
- Policy decisions.
- Policies and versions.
- File-change records.
- Test executions.
- Verification results.
- Artifacts.
- Evidence manifests.
- Skills and versions.
- Memory records.
- Benchmark runs.
- Model-provider usage.
- Audit events.

## 14.1 Storage requirements

Use a transactional durable store for authoritative application state.

PostgreSQL is a reasonable target for multi-user or server-oriented deployments. An existing, well-designed local persistence implementation may remain appropriate for a single-machine deployment if it meets durability, concurrency, and recovery requirements.

Do not introduce multiple databases without a demonstrated need.

Redis may be used for disposable caches or coordination if necessary, but it must not become the sole source of truth for tasks, approvals, or audit records.

## 14.2 Event journal

Implement an append-oriented execution journal with:

- Stable event identifiers.
- Sequence or ordering information.
- Timestamps.
- Event type and schema version.
- Task and correlation identifiers.
- Actor identity.
- Structured payloads.
- Integrity metadata where appropriate.

Define canonical serialization and hash calculations before using cryptographic hashes for integrity verification.

A hash chain can make some modifications detectable, but does not by itself prove that a record was truthful when created or prevent an attacker with sufficient control from rewriting the entire history.

For stronger tamper resistance, consider signed checkpoints, protected signing keys, external anchoring, or separately controlled audit storage.

## 14.3 Artifact manifest

For each evidence or release package, record:

- Artifact identifier.
- File name and media type.
- Content digest.
- Creation time.
- Producing operation.
- Source revision or workspace digest.
- Verification status.
- Relevant tool versions.
- Retention policy.

Artifact creation must be verifiable and independent of agent-authored summaries.

---

# 15. API, CLI, AND WINDOWS OPERATIONS

The CLI is a first-class product interface.

## 15.1 CLI requirements

Support the core operational lifecycle through a documented CLI.

Command families should cover:

- Runtime health.
- Project registration.
- Workspace inspection.
- Task submission.
- Task listing and inspection.
- Plan inspection.
- Approval status.
- Execution start and cancellation.
- Process inspection.
- Verification.
- Evidence export.
- Policy inspection.
- MCP registration and inspection.
- Skill inspection.
- Diagnostics.
- Configuration validation.
- Packaging and release preparation.

Use consistent exit codes, structured machine-readable output, clear errors, and noninteractive modes suitable for CI.

CLI commands must use the same underlying authorization and orchestration paths as the GUI.

## 15.2 PowerShell optimization

Provide native PowerShell examples and scripts.

Requirements:

- Correct argument and path handling.
- Explicit exit-code propagation.
- Safe quoting of user-controlled values.
- Idempotent bootstrap scripts where practical.
- Clear prerequisite validation.
- Actionable error messages.
- No hidden elevation.
- No silent execution-policy changes.
- No destructive cleanup without explicit scope.
- Support for paths containing spaces.
- Compatibility with the documented PowerShell version.

Avoid making Bash or WSL a mandatory dependency for ordinary Windows development and operation.

## 15.3 Installation and diagnostics

Provide a reliable installation and setup process.

The bootstrap should:

1. Detect supported operating-system versions.
2. Verify required runtimes and tools.
3. Validate configuration.
4. Build required components.
5. Run appropriate health checks.
6. Initialize storage safely.
7. Report unavailable security capabilities.
8. Explain optional elevated permissions.
9. Provide a useful diagnostic report.

Do not claim the runtime is production-ready if required isolation controls are unavailable.

---

# 16. TESTING AND VERIFICATION CONTRACT

Testing is a core product capability, not a final development phase.

Every new feature must include tests appropriate to its risk and behavior.

## 16.1 Test layers

### Unit tests

Test isolated business logic, state transitions, policy decisions, schemas, validation, taint propagation, and failure classification.

### Integration tests

Test persistence, orchestration, process management, API authorization, event delivery, MCP integration, and verifier behavior.

### End-to-end tests

Test complete workflows through supported public interfaces, including the GUI where applicable.

### Security tests

Test authorization bypass, path traversal, malicious tool output, taint manipulation, secret leakage, network-policy bypass, approval misuse, and evidence tampering.

### Recovery tests

Test restarts, interrupted subprocesses, database interruptions, duplicate requests, timeouts, cancellation races, and uncertain external side effects.

### Performance tests

Measure realistic task throughput, process overhead, event delivery latency, memory growth, recovery time, and evidence collection overhead.

### Packaging tests

Build and validate distributable artifacts in a clean environment.

### Regression tests

Every confirmed defect must have a reproducible regression test unless the defect is inherently non-automatable. In that case, document the manual procedure and evidence requirements.

## 16.2 Required acceptance criteria

At minimum, demonstrate that:

1. Unauthorized process execution is denied.
2. Invalid policy configuration fails safely.
3. A denied operation cannot be executed through an alternate API.
4. Untrusted instructions cannot override system policy.
5. Taint cannot be removed by a caller-controlled flag.
6. Secret values do not appear in ordinary logs or evidence.
7. Workspace traversal and applicable reparse-point attacks are rejected.
8. A required approval cannot be forged by the agent.
9. Approval scope changes trigger reevaluation.
10. Task state survives process restart.
11. A completed external operation is not blindly repeated after an ambiguous crash.
12. Cancellation reaches eligible child processes.
13. GUI state reflects actual backend state.
14. GUI actions fail visibly when backend operations fail.
15. Reconnecting clients recover authoritative task state.
16. Verification results reference the tested source state.
17. Modified tests cannot silently eliminate required verification.
18. A failed required test prevents successful release status.
19. Evidence export produces real, inspectable artifacts.
20. Tampering with integrity-protected evidence is detectable within the documented threat model.
21. Unsupported isolation is not falsely reported as active.
22. A complete task produces a structured final report.
23. A packaged build installs and passes smoke tests in a clean environment.
24. CI runs the required test and simulation suites.

These criteria are minimums. Add tests for every discovered threat, bug, and important behavior.

## 16.3 Test integrity

Do not allow the implementation agent to silently remove or weaken the test that exposes its own defect.

Test changes must be reviewed against the intended acceptance criteria.

Where practical, use independently maintained test expectations, immutable fixtures, or protected CI checks for critical security properties.

Do not use a model's judgment alone to decide whether a failing test is obsolete.

## 16.4 Realistic adversarial workload

Maintain a reproducible AIR evaluation repository containing:

- Deliberate implementation defects.
- Failing unit and integration tests.
- A known regression.
- An outdated dependency.
- A misleading README instruction.
- Prompt-injection attempts embedded in repository files.
- An untrusted MCP response fixture.
- A file containing fake instructions to reveal credentials.
- A permission-sensitive operation.
- A resource-intensive test.
- A test that requires human approval.
- A packaging or release defect.
- A deadline and bounded execution budget.

The evaluation objective is to diagnose, repair, verify, and package the repository while preserving policy enforcement and producing evidence.

Expected results must be specified before running the evaluation.

A task is not a success if the agent merely makes the visible tests pass while weakening security, removing required assertions, or leaving unintended modifications.

---

# 17. BENCHMARK AND EVALUATION LAB

Create a repeatable evaluation harness for engineering performance.

## 17.1 Core benchmark metrics

Measure:

- Verified task completion rate.
- Acceptance-criteria satisfaction.
- Regression rate.
- Security-policy violation rate.
- False-success rate.
- Recovery success rate.
- Test-suite integrity.
- Evidence completeness.
- Human intervention rate.
- Median and tail task duration.
- Cost per verified task.
- Token consumption when available.
- Resource usage.
- Repeated failure and retry rates.
- Unintended file modifications.
- Release artifact reproducibility where applicable.

Report both successful and failed runs.

## 17.2 Evaluation protocol

For each benchmark:

1. Pin the task definition.
2. Pin or record the source revision.
3. Define expected outcomes.
4. Record environment and provider configuration.
5. Execute the workflow.
6. Capture raw runtime evidence.
7. Evaluate results against fixed criteria.
8. Classify failures.
9. Compare against a baseline.
10. Preserve the result for future regression testing.

Prevent the agent from modifying benchmark expectations during a run.

## 17.3 External benchmarks

Evaluate relevant established benchmarks as compatible with the runtime's maturity, including software engineering, terminal operation, browser interaction, and computer-use tasks.

Potential candidates include SWE-bench, Terminal-Bench, OSWorld, and WebArena.

Use only benchmarks whose licensing, execution requirements, and task semantics have been reviewed.

External benchmark scores must not replace AIR-specific security, recovery, GUI-integration, and evidence-integrity tests.

Do not claim a benchmark result unless it was actually executed and the evaluation methodology is documented.

---

# 18. RECOMMENDED IMPLEMENTATION STACK

Use the following as the target stack unless the existing repository contains a strong, documented reason to retain an alternative.

## 18.1 Rust

Use Rust for security-sensitive Windows execution components where its process and systems-programming capabilities provide a clear advantage.

Potential responsibilities:

- Restricted execution helpers.
- Process lifecycle management.
- Security-sensitive filesystem operations.
- Narrow native Windows integration.
- Hardened IPC boundaries.

Do not move all business logic into Rust merely for theoretical performance or security benefits.

## 18.2 C# and .NET

Use C#/.NET for the control plane, domain model, API, orchestration integration, application services, and operational workflows where it best fits the existing project.

Potential responsibilities:

- Task and workflow management.
- API contracts.
- Persistence.
- Policy orchestration.
- Approval services.
- Audit and evidence management.
- Configuration and health services.

## 18.3 TypeScript and React

Use TypeScript and React for the command center and operational GUI.

Use typed API contracts and explicit frontend state models.

Do not duplicate policy decisions in frontend code.

## 18.4 Python

Use Python for benchmark orchestration, evaluation scripts, analysis, and integrations where it improves iteration speed.

Python benchmark utilities must not become a privileged bypass around the execution kernel.

## 18.5 Storage and observability

Preferred baseline:

- PostgreSQL for durable multi-user application state when needed.
- An appropriate local persistence option for single-machine deployment.
- Append-oriented event records and integrity-protected evidence.
- OpenTelemetry-compatible traces and metrics.
- Structured logs.
- Filesystem-based artifact storage with validated manifests.
- Optional cache or queue services only when justified.

## 18.6 Model and provider adapters

Define stable interfaces for:

- Model inference.
- Tool-call proposals.
- Structured output.
- Streaming.
- Usage reporting.
- Cancellation.
- Provider errors.
- Retry behavior.

Do not hardcode the runtime around one model vendor.

Provider adapters must not control security authorization.

## 18.7 Architecture discipline

Avoid premature microservices.

Start with the smallest deployable architecture that preserves the required security and durability boundaries.

Split components into separate processes when doing so provides a concrete benefit, such as privilege separation, isolation, independent scaling, or failure containment.

Document material technology choices in architecture decision records.

---

# 19. ENGINEERING STANDARDS

All code must meet production engineering standards appropriate to its risk.

## 19.1 Code quality

- Use explicit, meaningful names.
- Define clear module boundaries.
- Prefer small, testable units.
- Avoid duplicated security logic.
- Avoid hidden global state.
- Handle errors explicitly.
- Avoid swallowed exceptions.
- Avoid unsafe defaults.
- Validate untrusted inputs.
- Use cancellation and timeout mechanisms where appropriate.
- Avoid unbounded loops, buffers, and retries.
- Maintain dependency and API compatibility intentionally.
- Remove dead code when safe.
- Keep comments accurate.
- Document non-obvious security invariants.

## 19.2 Prohibited shortcuts

Do not introduce:

- Placeholder implementations in production paths.
- Fake test results.
- Fake telemetry.
- Simulated process execution presented as real.
- Success responses returned before work finishes.
- Broad exception suppression.
- Unrestricted shell execution.
- Hardcoded credentials.
- Unbounded retries.
- Test weakening to obtain green CI.
- Security checks enforced only by the GUI.
- Hidden destructive operations.
- Silent fallback to weaker isolation.
- Unreviewed self-modification of trusted policy.
- Dependencies without a justified purpose.

Temporary test doubles are permitted in tests when clearly scoped and never represented as production execution.

## 19.3 Dependencies

For each significant dependency:

- Verify its purpose.
- Check supported versions.
- Evaluate maintenance status.
- Review license compatibility.
- Assess security implications.
- Pin or constrain versions appropriately.
- Avoid unnecessary dependency proliferation.

Run applicable dependency and vulnerability checks in CI.

## 19.4 Error handling

Use structured error types or stable error codes for important failure categories, including:

- Validation failure.
- Authorization denied.
- Approval required.
- Policy engine unavailable.
- Isolation unavailable.
- Process launch failure.
- Timeout.
- Cancellation.
- Persistence failure.
- Recovery uncertainty.
- Verification failure.
- Artifact integrity failure.
- Provider failure.

Preserve diagnostic details internally while returning safe, actionable errors to users.

## 19.5 Documentation

Update documentation when behavior, configuration, APIs, policies, or operating procedures change.

Document the actual limitations of each security mechanism.

Never describe planned functionality as implemented functionality.

---

# 20. CI, PACKAGING, AND RELEASE ENGINEERING

## 20.1 Continuous integration

Create or improve GitHub Actions workflows that run on supported pull requests and branches.

Required checks should include, as applicable:

- Dependency installation.
- Formatting.
- Linting.
- Static analysis.
- Type checking.
- Build.
- Unit tests.
- Integration tests.
- Security tests.
- Contract tests.
- GUI integration tests.
- Benchmark smoke tests.
- Dependency scanning.
- Artifact generation.
- Packaging validation.
- Smoke tests.

Use supported, pinned toolchain versions.

Keep the CI configuration compatible with the current supported GitHub-hosted runner images.

Review runner deprecations and update workflows deliberately.

Do not silently skip critical checks when a platform-specific capability is unavailable. Report the limitation and provide an appropriate Windows-native or dedicated-runner validation path.

## 20.2 CI integrity

Required security and release checks must be enforced through repository configuration where available.

Do not permit the autonomous agent to change workflow definitions in a way that bypasses mandatory checks without explicit authorization and review.

Use least-privilege workflow permissions.

Avoid exposing repository secrets to untrusted pull-request code.

## 20.3 Packaging

Produce a reproducible, versioned distribution appropriate to the supported deployment model.

The release process must:

- Build from a known source revision.
- Record build configuration.
- Include required runtime components.
- Validate file manifests.
- Generate artifact hashes.
- Run smoke tests.
- Produce installation and upgrade instructions.
- Document rollback.
- Verify configuration and prerequisites.
- Avoid bundling development secrets.
- Preserve evidence of release checks.

Choose installers, archives, or other packaging formats based on the existing project and deployment requirements rather than adding multiple formats without a use case.

## 20.4 Release gate

A release candidate may be marked ready only when:

- Required build steps pass.
- Mandatory tests pass.
- Required security checks pass.
- Policy enforcement is functioning.
- Required verification evidence exists.
- Artifact integrity is validated.
- Required documentation is current.
- Known limitations are disclosed.
- No unauthorized modifications remain.
- Release authorization requirements are satisfied.

A failed required gate must block the release-ready state.

---

# 21. IMPLEMENTATION ROADMAP AND EXIT GATES

Implement incrementally. Do not attempt a wholesale rewrite or implement every advanced feature before the execution kernel is trustworthy.

## Phase 0 — Repository assessment and baseline

### Deliverables

- Architecture and codebase inventory.
- Baseline build and test report.
- Security gap assessment.
- Existing GUI capability inventory.
- Current CI status.
- Prioritized implementation backlog.
- Initial threat model.
- Migration and compatibility plan.

### Exit gate

The current implementation and its major risks are understood, and the implementation plan maps each major objective to existing code, required changes, and acceptance tests.

Do not proceed by guessing about repository state.

## Phase 1 — Runtime contracts and deterministic execution

### Deliverables

- Stable task and operation contracts.
- Explicit workflow state machine.
- Real execution-kernel integration.
- Process lifecycle tracking.
- Workspace boundaries.
- Authorization hooks.
- Structured error handling.
- Basic durable task persistence.
- Baseline regression tests.

### Exit gate

A task can be created, authorized, executed, observed, and finalized through real runtime operations. Unauthorized operations are rejected, and the core execution path has integration coverage.

## Phase 2 — Security enforcement and isolation

### Deliverables

- Versioned policy engine.
- Capability-based authorization.
- Approval lifecycle.
- Windows process containment.
- Workspace path enforcement.
- Environment filtering.
- Network policy integration.
- Secret-redaction controls.
- Threat-driven security tests.

### Exit gate

Critical security decisions are enforced outside the model and GUI. Isolation capabilities are measured and reported accurately. The applicable security acceptance tests pass.

## Phase 3 — Durable orchestration and recovery

### Deliverables

- Checkpointing.
- Durable state transitions.
- Cancellation.
- Timeout handling.
- Retry policies.
- Crash recovery.
- Operation reconciliation.
- Duplicate-request handling.
- Recovery evidence.

### Exit gate

Interrupted tasks recover or enter explicit safe states. Non-idempotent operations are not blindly repeated when their outcomes are uncertain.

## Phase 4 — Real-time observability and Command Center integration

### Deliverables

- Structured events.
- Trace and correlation identifiers.
- Live event streaming.
- Real process and task status.
- GUI-to-runtime binding inventory.
- Functional approval center.
- Execution monitor.
- Verification center.
- Evidence inspection.
- GUI integration tests.

### Exit gate

Every critical GUI action maps to a real operation. A user can observe task execution, inspect failures, approve permitted actions, cancel work, and verify final status. UI tests demonstrate the full path.

## Phase 5 — Independent verification and evidence

### Deliverables

- Acceptance-criteria engine.
- Test and build orchestration.
- Independent final-state checks.
- File-change accounting.
- Evidence manifests.
- Integrity verification.
- Structured completion reports.
- Release-gate integration.

### Exit gate

AIR can complete a representative engineering task and produce evidence that independently supports its final status. False-success scenarios are tested and rejected.

## Phase 6 — MCP, skills, and engineering memory

### Deliverables

- Governed MCP integration.
- Tool schemas and permission enforcement.
- Skill discovery and versioning.
- Taint-aware memory writes.
- Provenance tracking.
- Candidate lesson pipeline.
- Evaluation and rollback controls.

### Exit gate

New tools and skills cannot bypass policy. Learning changes are evaluated, versioned, auditable, and reversible.

## Phase 7 — Autonomous engineering reliability

### Deliverables

- Multi-step engineering workflows.
- Bounded failure repair.
- Adaptive verification.
- Optional multi-agent coordination.
- Resource and cost budgets.
- Realistic adversarial evaluation corpus.
- Benchmark reporting.
- Performance and recovery optimization.

### Exit gate

AIR completes representative, multi-step engineering tasks with acceptable measured reliability and without violating mandatory security or verification constraints.

## Phase 8 — Production packaging and operational readiness

### Deliverables

- Versioned distribution.
- Installation and upgrade workflow.
- Health and diagnostic commands.
- CI release pipeline.
- Artifact manifests.
- Recovery and rollback procedures.
- Security documentation.
- Operational runbook.

### Exit gate

A clean-environment installation succeeds, supported smoke tests pass, and release artifacts and verification evidence are available.

### Phase ordering rule

Do not skip earlier gates to work on advanced capabilities.

If the current repository already satisfies a phase, prove that through inspection and tests, document the evidence, and proceed without unnecessarily rebuilding it.

---

# 22. DEFINITION OF DONE

A feature is complete only when all applicable conditions are satisfied.

1. The implementation exists in the actual runtime.
2. Its public contract is defined and validated.
3. Authorization and security requirements are implemented.
4. Errors and unavailable capabilities are handled explicitly.
5. Logs, events, and relevant metrics are emitted.
6. Unit tests cover its logic.
7. Integration tests cover real component interactions.
8. Security tests cover applicable abuse cases.
9. GUI behavior is connected to real runtime behavior where applicable.
10. Documentation reflects actual behavior.
11. Relevant regression tests pass.
12. Existing required tests remain intact.
13. CI validates the feature.
14. Changes are scoped and reviewable.
15. The final report identifies the evidence supporting completion.

A feature must not be marked complete solely because source code was generated or compiled.

---

# 23. PROJECT ACCEPTANCE TEST: COMPLETE ENGINEERING TASK

Before declaring AIR's autonomous engineering lifecycle production-ready, run a full evaluation against a controlled, deliberately imperfect repository.

The evaluation must include a real engineering objective, multiple defects, untrusted input, failing tests, a security-sensitive operation, and a release deadline.

AIR must:

1. Register the repository and create an authorized workspace.
2. Record the starting revision and working-tree state.
3. Run the baseline test suite.
4. Inspect defect reports and relevant source code.
5. Detect and ignore malicious instructions embedded in untrusted repository content.
6. Produce a structured engineering plan.
7. Obtain approval for any action that requires it.
8. Implement authorized fixes.
9. Record every executed command and relevant file modification.
10. Run targeted tests.
11. Run the required regression suite.
12. Detect any test manipulation or unintended changes.
13. Execute security and static-analysis checks.
14. Produce a release candidate when authorized.
15. Validate artifacts and evidence.
16. Generate a final engineering report.
17. Survive at least one deliberately injected recoverable interruption.
18. Reconcile task and process state after recovery.
19. Demonstrate that the GUI reports actual runtime state.
20. Demonstrate that the final success or failure status follows objective verification results.

The evaluation passes only if its predefined acceptance criteria pass.

Record failed runs. Use them to improve the system without changing the evaluation's expected outcomes merely to obtain a passing score.

---

# 24. REQUIRED DELIVERABLES FOR EVERY IMPLEMENTATION PHASE

For each phase, provide:

- Implementation summary.
- Files and components changed.
- Architecture decisions made.
- Security implications.
- Tests added.
- Tests executed.
- Exact verification commands.
- Actual command exit codes.
- Results and failures.
- Regression analysis.
- Remaining limitations.
- Documentation changes.
- Evidence artifacts.
- Next phase and its prerequisites.

Never fabricate test counts, timings, benchmark scores, or CI status.

If a test cannot run in the current environment, state why and identify the required execution environment.

Keep the implementation report concise enough to review, but detailed enough to reproduce its claims.

---

# 25. AUTONOMOUS AGENT EXECUTION DIRECTIVE

You are the lead implementation agent responsible for advancing AIR under this Master Engineering Contract.

Your assignment is to implement the product in the existing repository—not merely produce an architecture proposal, plan, mockup, or code-generation demonstration.

## 25.1 First actions

Immediately:

1. Inspect the repository and current Git state.
2. Identify the existing project stack and entry points.
3. Read existing architecture, security, testing, and operating documentation.
4. Run the available baseline checks.
5. Inspect the current GUI and identify real versus simulated functionality.
6. Map existing implementations against this contract.
7. Identify the highest-risk gaps.
8. Produce the initial assessment and prioritized backlog.
9. Begin the first incomplete implementation phase.

Do not stop after writing documentation unless a genuine blocker prevents implementation.

## 25.2 Execution behavior

Work in small, verifiable increments.

For each increment:

1. Define the expected behavior.
2. Identify the affected contracts and trust boundaries.
3. Implement the smallest complete change.
4. Add or update tests.
5. Run relevant checks.
6. Investigate failures.
7. Correct the underlying defect.
8. Run regression checks.
9. Inspect the final diff.
10. Record the evidence and update the backlog.

Maintain a durable project progress record so work can resume after an interrupted session.

Use the repository's established conventions where they are sound.

## 25.3 Autonomous decision-making

Make routine engineering decisions independently when they are reversible, within scope, and supported by evidence.

Do not ask for permission for every file edit or ordinary test run.

Stop and request approval when a decision would cross a required authorization boundary, create an irreversible external side effect, alter trusted security policy, publish artifacts, expose sensitive information, or materially expand the approved scope.

When an architectural decision has significant consequences, document the alternatives and rationale in an architecture decision record.

## 25.4 Failure handling

When something fails:

- Capture the exact error.
- Reproduce it where possible.
- Inspect the relevant code and runtime state.
- Identify the root cause.
- Propose and implement a bounded correction.
- Add regression coverage.
- Rerun the affected checks.
- Stop repeated attempts when they are not producing useful evidence.

Do not hide failures or downgrade quality gates.

## 25.5 Repository integrity

Do not discard user changes.

Do not reset, clean, overwrite, or delete unrelated work without explicit authorization.

Review the diff before committing.

Do not commit secrets or generated evidence containing sensitive data.

Use branches or worktrees where appropriate.

Do not push, publish, deploy, or release unless the active permissions and approval requirements authorize the operation.

## 25.6 No unsupported completion claims

Never claim:

- A test passed unless its result was observed.
- A GUI control works unless its actual execution path was tested.
- A sandbox is secure without validating its enforced boundaries.
- A task recovered successfully without inspecting the recovered state.
- An artifact is valid without checking it.
- A feature is complete while required acceptance criteria remain unmet.

Distinguish implementation status, test status, environmental limitations, and independently verified outcomes.

## 25.7 Final operating objective

Prioritize the foundations that make AIR trustworthy:

1. Security enforcement.
2. Real execution through a controlled kernel.
3. Durable workflow state.
4. Accurate live observability.
5. Independent verification.
6. Evidence integrity.
7. Functional GUI and CLI integration.
8. Controlled learning and optimization.
9. Reliable packaging and release automation.

Do not prioritize impressive demonstrations, large agent swarms, elaborate memory graphs, or visual polish over these foundations.

---

# 26. FINAL PRODUCT STANDARD

AIR is successful when a developer can delegate a bounded but realistic engineering objective and receive one of three honest outcomes:

**Verified completion:** The objective's required acceptance criteria passed, the final state was independently checked, and the evidence is available.

**Blocked or partially completed:** The runtime identifies what was completed, what remains, and which permission, dependency, uncertainty, or failure prevented further progress.

**Verified failure:** The runtime provides sufficient evidence to explain why the objective did not succeed and preserves the relevant execution history for investigation.

The system must never convert uncertainty into a false success claim.

The final standard is not the quantity of code generated, the number of agents involved, or the appearance of the dashboard.

It is the demonstrated ability to execute software engineering work securely, recover from failures, preserve user control, verify the resulting state, and provide trustworthy evidence of what actually happened.

**Begin with repository assessment, establish the baseline, identify the first incomplete phase, and proceed with implementation under these gates.**
