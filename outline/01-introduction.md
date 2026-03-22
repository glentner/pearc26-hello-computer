---
status: draft
target_words: 400
actual_words: ~400
citations:
  - openai2022chatgpt  # ChatGPT launch (used)
  - yao2023react       # ReAct agentic definition (used)
  - openai2023gpt4     # GPT-4 (used)
  - anthropic2024claude3  # Claude 3 (used)
---

# Introduction: "Shall We Play a Game?"

## Key Points
- The moment: AI crossed a threshold into practical utility for developers/researchers
- Public accessibility was the inflection point, not the technology itself
- Multimodal era bridged chatbots and agents
- HPC centers face a choice: ignore, prohibit, or engage

## Notes
- "Shall We Play a Game?" - WarGames (1983), WOPR/Joshua
- Sets the tone: we're playing a new game with new rules
- Merged the short 2-sentence paragraph into main flow (FB-1.09, FB-3.07)
- Removed "from the trenches" (FB-1.08)
- "Minimal human intervention" softened to "increasing sophistication" (FB-3.05)

## Subsection: "Mostly Harmless" (Motivations)

### Key Points
- Cautious optimism: the tools themselves are mostly safe
- Frontier AI follows policy more reliably than users (FB-2.10)
- Dog-fooding: use the tools ourselves for visceral understanding (FB-1.11)
- Agent-first workflow narrative woven in (FB-2.05)

### Notes
- "Mostly Harmless" - Hitchhiker's Guide to the Galaxy (Douglas Adams)
- Realigned: argument is "tools are good" not "resistance is futile" (FB-1.10)
- Toned down closing per FB-3.09

## Draft

### Shall We Play a Game?

On November 30, 2022, OpenAI released ChatGPT as a "research preview." Within five days
it had one million users; by January 2023, one hundred million, the fastest-growing
consumer application in history. The inflection point was not the technology itself but
its sudden public accessibility: for the first time, anyone could converse with a frontier
language model.

For those of us supporting researchers on high-performance computing systems, the
implications arrived slowly and then all at once. At first, ChatGPT was a curiosity, a
toy that could write passable Python functions or explain error messages with varying
degrees of accuracy. Then came GPT-4, Claude, and their competitors, each iteration more
capable than the last. Models became multimodal, processing images, audio, and video
alongside text. Then came *agentic* AI: systems that don't just respond to prompts but
reason, plan, and execute multi-step workflows autonomously. Today's agentic development
environments (Warp, Cursor, Claude Code) can read files, run shell commands, edit code,
and iterate toward solutions with increasing sophistication. HPC centers now face a
question with no precedent in our field: how do we engage with tools that can, in some
cases, do our jobs faster than we can?

### Mostly Harmless

The Hitchhiker's Guide to the Galaxy famously summarized Earth in two words: "Mostly
Harmless." We adopt this as our working hypothesis for agentic AI in HPC.

Our assessment at Purdue's Rosen Center for Advanced Computing (RCAC) is that these tools
are, in fact, mostly harmless. Frontier AI systems follow instructions more reliably than
many users do: they respect queue policies, observe resource limits, and avoid dangerous
operations when properly configured. The greater risk lies in disengagement. A graduate
student debugging a CUDA kernel at 2 AM will reach for ChatGPT whether or not we endorse
it. If we don't shape the context in which that interaction occurs, we leave both the
student and the cluster exposed to preventable mistakes.

We chose proactive engagement. We use these tools ourselves, daily, so that we have
visceral understanding of their capabilities and limitations. This paper is itself a
product of that practice: an agent-first workflow comprising rules files, session logs,
annotated references, and iterative revision, all documented in a public GitHub
repository. This paper documents our early experience deploying system-wide configurations,
custom MCP (Model Context Protocol) servers, and user guidance. We offer this as both
evidence and invitation.
