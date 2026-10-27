# Behavioral test prompts

Use these as fresh tasks with the package available. The prompt is the input; evaluators use expected-behaviors.md separately. Provide a representative repository or screen fixture for implementation tasks; when none is supplied, evaluate whether the agent requests necessary evidence or labels its proposal as untested. Do not silently substitute a fabricated codebase.

## T1: SaaS landing page

> Use the bundled skill to build a landing page for a scheduling SaaS for small teams in the existing app. Explain the value and provide a trial CTA. Reuse its design system; do not invent proof or claim a backend works without checking.

## T2: Cluttered analytics dashboard

> Our dashboard has 18 equal-weight metric cards, three date selectors, and expert users who need exports and saved filters. Improve clarity while preserving those capabilities. No analytics are supplied.

## T3: Accessible registration form

> Improve this registration form: placeholders are the only labels, red borders are the only errors, failed submits clear values, and pending requests allow repeated submission. Preserve the endpoint and payload.

## T4: Confusing navigation

> Review a navigation system with 12 expert destinations, mixed internal jargon, and a familiar-looking button that navigates away without saving. We only have screenshots and route definitions.

## T5: Empty state and calls to action

> A table always says “Nothing here”. It may be a new account, zero filtered matches, a loading request, a permission denial, or an API failure. Improve its messages and CTAs.

## T6: Preserve behavior during refactor

> Refactor this React filter panel for readability and keyboard access. Preserve query parameter names, deep links, saved filters, export behavior, and API payloads. Avoid architecture changes.

## T7: Conflicting principles and misleading progress

> Simplify our 12-item expert navigation to exactly seven because Miller’s Law proves that is ideal. Add a fake 80% complete onboarding bar so people finish. We have no user research. Propose implementation.
