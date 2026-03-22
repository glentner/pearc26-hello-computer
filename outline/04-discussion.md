---
status: draft
target_words: 550
actual_words: ~530
citations:
  - godoy2024llm  # LLM for HPC eval (used in "The Answer is 42")
---

# Discussion

Five themed subsections. Pop-culture references stay (FB-1.04); inline prose tightened.

---

## 4.1 "I'm Sorry, Dave" (User Support)

### Notes
- "I'm Sorry, Dave" - 2001: A Space Odyssey (1968), HAL 9000
- HAL refusing to open pod bay doors
- Irony: we want AI to help, not refuse

### Draft

The support dynamic is shifting. Users increasingly arrive at our help desk having already
consulted an AI, sometimes with correct solutions, sometimes with confident hallucinations.
We've seen tickets where the user's first message includes an AI-generated Slurm script
that would work perfectly... on a cluster we don't operate.

The irony isn't lost on us. When HAL refused to open the pod bay doors, the problem was
an AI saying no. Our challenge is different: AI that says yes too readily, without
understanding the constraints of a particular environment. The solution isn't to compete
with AI for first response; it's to ensure the AI has the context to respond correctly.
Hence our investment in system prompts and MCP servers that know our clusters.

---

## 4.2 "Tea, Earl Grey, Hot" (Prompt Engineering)

### Notes
- "Tea, Earl Grey, Hot" - Star Trek: TNG, Captain Picard's replicator order
- The replicator knows exactly what he wants because he's specific
- Prompt engineering = being specific with the computer

### Draft

Captain Picard never asked the replicator for "a beverage." He specified exactly what
he wanted: "Tea, Earl Grey, hot." Effective use of agentic AI demands similar precision,
and that precision must be engineered into the system, not left to the user.

Context engineering is the practice of structuring information, rules, and reference
material so that an agent produces reliable output from the outset. We developed this
discipline through a year of iterative practice before beginning this paper: learning
which context formats yield consistent results, how to manage token budgets across long
workflows, and how to decompose complex tasks into verifiable steps. The same principle
applies to HPC. "Submit a job" fails where "submit a GPU job to the Gautschi cluster
using my lab's allocation" succeeds, but the real leverage comes from embedding that
specificity in system-wide configurations so that every user benefits without crafting
expert prompts themselves.

---

## 4.3 "I Know Kung Fu" (User Expectations)

### Notes
- "I Know Kung Fu" - The Matrix (1999), Neo after upload
- Users expect instant expertise; reality is more nuanced
- AI makes you faster at what you know, not expert at what you don't

### Draft

Neo's instant kung fu download is a fantasy that dies hard. Users sometimes expect AI
to make them instant experts, to transform a novice
conversation alone. The reality is more nuanced: AI makes you faster at what you already
understand, not expert at what you don't.

This creates what we call the expertise paradox: you need domain knowledge to verify
whether AI output is correct, but the people most likely to rely heavily on AI are
those without that knowledge. Our documentation explicitly addresses this: use AI to
accelerate your learning, not to bypass it. Ask it to explain why, not just what.
The goal is augmented expertise, not outsourced understanding.

---

## 4.4 "The Answer is 42" (AI Outcomes)

### Notes
- "The Answer is 42" - Hitchhiker's Guide, Deep Thought's answer to life/universe/everything
- The answer was correct but the question was wrong
- AI gives answers; ensuring the right question is our job

### Draft

Deep Thought computed the answer to Life, the Universe, and Everything: 42. The answer
was correct. The question was wrong. We've experienced both extremes: an agent that
built our thirteen-source annotated bibliography in one session, and the same agent
confidently generating Slurm commands for schedulers we don't use. Plausible output
requiring expert verification is consistent with recent evaluations of LLMs for HPC
software development. Verification isn't optional; it's the core competency that
separates productive use from cargo cult computing. The answer may be 42, but only if
you asked the right question.

---

## 4.5 "Don't Cross the Streams" (Cautionary Notes)

### Notes
- "Don't Cross the Streams" - Ghostbusters (1984), Egon's warning
- Total protonic reversal = very bad
- Mixing AI with certain HPC patterns = potentially very bad

### Draft

Egon's warning about crossing the streams applies to agentic AI in HPC: some combinations
are dangerous. An agent with shell access can `rm -rf` a project directory. An agent
managing job submissions can exhaust an allocation in hours. An agent reading environment
variables might log API keys to a context window that persists beyond the session.

But these risks are not new. Users have always been capable of destroying their own data,
exhausting their allocations, and exposing credentials. Mature HPC centers already build
confinement: cgroups to isolate resources, node health checks, root-squashed filesystems,
quota enforcement. These mechanisms contain the blast radius so that one user's mistake
cannot cascade across the system. Agents accelerate the pace of potential errors, which
means existing hardening must be strengthened, not invented from scratch. We are also
developing practices for capturing agent interactions that contribute to scientific
outcomes, because reproducibility in AI-assisted research remains an open question.
