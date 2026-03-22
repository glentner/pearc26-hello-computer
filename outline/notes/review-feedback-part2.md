---
source: reviews/review_phase_1_part_2.md
reviewed_by: [Geoffrey R. Lentner, Ashish Ashish]
date: 2026-03-21
---

# Review Feedback: Part 2

## Section: Background (recap)

### [FB-2.01] Section 2 reconfirmed as solid
- **Type**: meta
- **Severity**: consider
- **Quote/context**: Geoffrey: "this is really information dense. I think the signal to noise is really high and I don't have any complaints with the flow... it's just kind of matter of fact. And I think that's fine."
- **Action**: No content changes. Reconfirms FB-1.13.

## Section: Abstract / Introduction — AI-authorship disclosure

### [FB-2.02] Need stronger AI-authorship statement in abstract
- **Type**: framing
- **Severity**: must-fix
- **Quote/context**: Ashish asks whether the paper acknowledges "this is entirely done by agents" because "right now it feels like we are portraying that it's done by us." Geoffrey agrees: "we need to put it in the abstract and the introduction."
- **Action**: Add a punchy, enticing statement about agent-first authorship in the abstract. Not "agentic assistance" — convey that the entire paper emerged from a documented agentic workflow. Reinforces FB-1.12.

### [FB-2.03] AI-authorship reveal strategy — punchy opener vs. mic-drop ending
- **Type**: framing
- **Severity**: must-fix
- **Quote/context**: Ashish proposes two options: (a) hint in the abstract and reveal fully at the end as a mic-drop, or (b) be upfront from the start. Discussion of storytelling — "how you start and how you end." Geoffrey leans toward a punchy statement early in the abstract but with the detailed workflow narrative deferred to the closing.
- **Action**: Resolved in plan — punchy enticing statement in abstract ("come see what an agent-first paper looks like"), detailed workflow/harness/GitHub narrative in closing statements, ACM policy compliance in acknowledgments.

### [FB-2.04] "Agentic assistance" repeated — reframe all occurrences
- **Type**: word-choice
- **Severity**: must-fix
- **Quote/context**: Geoffrey: "this right here, I want to rephrase this to your point — not to say 'agentic assistance,' but to say — like, we need a stronger statement." Occurs in abstract, intro, and conclusion.
- **Action**: Systematic replacement of "agentic assistance" with agent-first language across all three occurrences. Reinforces FB-1.12.

## Section: Structure / Paper-level

### [FB-2.05] Missing agentic workflow narrative — the paper's unique contribution
- **Type**: content
- **Severity**: must-fix
- **Quote/context**: Geoffrey: "what maybe we should lean into more... is to speak more directly to the process. Because part of it is about agentic workflows, but between the historical retrospective and an enumeration of the things that we're doing, we don't really take that much time to spell out what does that even mean." He details: 68 commits, 6 hours on rules of engagement before writing a single word, 30 hours of research and planning. "That process and how it all connects is part of what this is supposed to be."
- **Action**: Add a paragraph (likely in the Introduction or early Approach) describing the actual agent-first workflow — rules, commits, session logs, the extensive research phase before any prose was generated. This is the paper's unique contribution and is underrepresented in the first draft.

### [FB-2.06] Acknowledgment section tone — make it a "by the way" reveal
- **Type**: tone
- **Severity**: should-fix
- **Quote/context**: Geoffrey: "we could kind of change the tone of this to be more of the 'oh and by the way.'" Ashish worries "four of them are not even going to look there" — risk of the disclosure being missed if only in acknowledgments.
- **Action**: The acknowledgment section keeps ACM compliance language but the *meaningful* disclosure lives in the abstract and closing statements. Acknowledgments become secondary, not primary, vehicle for the AI-authorship reveal.

## Section: Approach

### [FB-2.07] Three pillars are accurate and verbatim from author intent
- **Type**: meta
- **Severity**: consider
- **Quote/context**: Geoffrey: "these are basic... the MVP of these already exists and is on public — these are publicly accessible GitHub repos now." The three pillars (system-wide configs, MCP servers, user documentation) are confirmed.
- **Action**: No structural change to the three-pillar approach. Update status: MCP repos are now public/beta (no longer pre-alpha).

### [FB-2.08] System-wide configuration — word choice could be stronger
- **Type**: word-choice
- **Severity**: should-fix
- **Quote/context**: Geoffrey: "the wording is kind of not weak — I think the word choice could be stronger and more elegant. Not over the top flowery... I just mean it's a little weaker than it needs to be."
- **Action**: Tighten prose in Section 3.1. Make language more direct and confident without being flowery.

### [FB-2.09] Name-drop `agents.d` directory concept
- **Type**: content
- **Severity**: consider
- **Quote/context**: Geoffrey: "I'm going to name-drop my intended — I want that to catch on. An agents.d folder that is a directory full of markdown files that are system-wide on all clusters."
- **Action**: Consider mentioning the `/etc/agents.d` naming convention as a concrete example of the system-wide configuration approach.

### [FB-2.10] Agent compliance is better than user compliance
- **Type**: content
- **Severity**: should-fix
- **Quote/context**: Geoffrey on the last bit of Section 3.1: "the agents are acting on your behalf, and they will abide better than you at what they're supposed to do. Which is kind of funny."
- **Action**: Reinforce this point in the approach or discussion — agents follow policy more reliably than users do, which is itself an argument for engagement.
