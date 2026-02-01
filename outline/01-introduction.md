---
status: review
target_words: 400
actual_words: ~370
---

# Introduction: "Shall We Play a Game?"

## Key Points
- The moment: AI has crossed a threshold into practical utility for developers/researchers
- HPC centers face a choice: ignore, prohibit, or engage
- Framing the paper's dual nature: technical report + personal narrative
- Title reference: Star Trek IV's Scotty talking to a 1980s computer

## Notes
- "Shall We Play a Game?" - WarGames (1983), WOPR/Joshua
- Sets the tone: we're playing a new game with new rules
- The question isn't whether AI will be used—it's how we shape that use

## Subsection: "Mostly Harmless" (Motivations)

### Key Points
- "If you can't beat them, join them" philosophy
- Proactive enablement vs. reactive prohibition
- Users will bring these tools regardless—better to guide than ignore
- Personal motivation: genuine excitement + professional responsibility
- 8-12 weeks deep dive as Principal AI Scientist at RCAC

### Notes
- "Mostly Harmless" - Hitchhiker's Guide to the Galaxy (Douglas Adams)
- Earth's entry in the Guide: first "Harmless", updated to "Mostly Harmless"
- Fits our cautious optimism: AI is mostly harmless... with caveats

## Draft

### Shall We Play a Game?

On November 30, 2022, OpenAI released ChatGPT as a "research preview." Within five days
it had one million users; by January 2023, one hundred million—the fastest-growing
consumer application in history. The game changed overnight.

For those of us supporting researchers on high-performance computing systems, the
implications arrived slowly and then all at once. At first, ChatGPT was a curiosity—a
curious toy that could write passable Python functions or explain error messages with
varying degrees of accuracy. Then came GPT-4, Claude, and their competitors, each
iteration more capable than the last. Then came *agentic* AI: systems that don't just
respond to prompts but reason, plan, and execute multi-step workflows autonomously.
Today's agentic development environments—tools like Warp, Cursor, and Claude Code—can
read files, run shell commands, edit code, and iterate toward solutions with minimal
human intervention.

HPC centers now face a question with no precedent in our field: how do we engage with
tools that can, in some cases, do our jobs faster than we can? This paper offers one
answer from the trenches.

### Mostly Harmless

The Hitchhiker's Guide to the Galaxy famously summarized Earth in two words: "Mostly
Harmless." We adopt this as our working hypothesis for agentic AI in HPC workflows.

At Purdue's Rosen Center for Advanced Computing (RCAC), we chose proactive engagement
over prohibition. Our reasoning was simple: users will bring these tools regardless of
policy. A graduate student debugging a CUDA kernel at 2 AM will reach for ChatGPT whether
or not we endorse it. The question is whether we help them use it effectively—or leave
them to discover its hallucinations the hard way.

This paper documents our early experience: system-wide configurations that expose cluster
metadata to agentic tools, custom MCP (Model Context Protocol) servers that provide
contextual help, and the lessons learned from using these tools ourselves—including
writing this very paper with agentic assistance. We offer this as both practical
guidance and invitation: the game is afoot, and HPC centers that engage early will shape
the rules.
