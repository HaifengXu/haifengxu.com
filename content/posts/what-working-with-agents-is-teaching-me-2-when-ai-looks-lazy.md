+++
title = "What Working with Agents Is Teaching Me #2: When AI Looks Lazy"
date = 2026-04-10T23:28:59-07:00
draft = false
description = "What looks like laziness in AI agents is often overload: bounded systems losing track of the right state as tasks and context grow."
tags = ["ai", "judgment"]
categories = ["AI", "Thinking"]
toc = true
readingTime = true
featured = false
+++
![Context overload diagram](/posts/what-working-with-agents-is-teaching-me-2-when-ai-looks-lazy/ngjq2jqcjcbjs98xvd4mmx.png)

Working with AI agents keeps exposing a pattern that feels familiar. An agent misses a constraint that was already stated, stops before the task is actually complete, or produces something that looks polished until a closer read reveals that it does not hold up. The first reaction is often to call that behavior lazy. After spending more time with agents, that explanation feels too shallow.

A better explanation is overload. As the task grows, the agent has more observations to track, more side paths to reconcile, and more stale or half-correct state to carry forward. That makes the failure feel less alien, because the same pattern shows up in people.

> What looks like laziness is often a bounded system losing track of the right things.

## Where the agent starts to degrade

Many agent runs begin well. Early in the process, the goal is clear, the constraints are fresh, and the active state is still small enough to fit into a coherent working set. Under those conditions, the agent can look fast, capable, and surprisingly effective.

Trouble usually starts when the run stretches out. The thread gets longer. Tool outputs accumulate. Old assumptions remain in the background even after they should have been discarded. Earlier instructions compete with later adjustments. At some point, the system stops reasoning cleanly across the whole task and starts leaning on the **most recent, most obvious, or easiest-to-reach information**. Important details from earlier in the run get dropped. Completion gets declared before the real work is done.

That moment is easy to describe as the model getting dumb. In many cases, the deeper issue is context failure rather than lack of raw intelligence. A larger context window helps, but more room does not automatically create better use of the room. Capacity and clarity are different things. A bigger desk is only useful when the important documents stay visible and organized. Once the desk is covered with half-relevant papers, more surface area mostly creates more clutter.

The more time I spend with agents, the more this looks like the central bottleneck. Raw model intelligence matters, but the practical limit often comes from whether the system can keep the right information active at the right moment.

## Why “lazy” is the wrong word

The word “lazy” captures the feeling of the failure, but not the mechanism. A lot of agent behavior looks more like satisficing than refusal. The system finds something plausible enough to continue with, or plausible enough to stop with, instead of doing the extra work required to verify that it is actually correct.

Human behavior under load often looks similar. A person faced with too many moving parts will stop exploring the full space of options, settle for the first answer that seems reasonable, skip a check that would have helped, or lose track of a subtle constraint that had been clear earlier. That does not always reflect low effort. It often reflects a limit in what can be kept active and coordinated at once.

Working with agents has made that clearer to me. People do not perform well by holding everything in working memory. Notes, checklists, habits, tools, routines, teammates, and pauses all reduce the amount that has to be actively managed in the head. External support is not a minor convenience. External support is part of how reliable thinking happens.

> Intelligence depends heavily on support for bounded cognition.

The same principle applies to agents. Similarity does not make agents human. Similarity does suggest that bounded systems benefit from scaffolding.

## The wrong mental model for progress

A lot of discussion about agents still assumes that the main path forward is a smarter model paired with a larger context window. Better models and larger windows will help. That framing still misses where many practical gains are likely to come from.

A more useful mental model centers the harness. **Context structuring, indexing, retrieval, memory, handoffs, and verification** all shape whether the model can behave like a reliable worker over time. The model is not the entire worker. The model is one component in a larger system.

A human comes with memory, attention, motivation, sensory grounding, habits, self-monitoring, and social awareness all bundled together, even if imperfectly. An agent does not arrive with that package. The harness has to decide what to show, what to hide, what to store, what to retrieve, when to summarize, when to reset, when to verify progress, and what counts as done. Those choices are not minor implementation details. Those choices are part of the intelligence of the overall system.

That is why the harness increasingly feels analogous to workplace design for people. A badly designed environment creates unnecessary cognitive burden. A well-designed environment keeps the right things visible, reduces avoidable load, and makes good judgment easier to sustain.

## What better work with agents looks like

The practical lesson is straightforward: do not expect the agent to carry the whole task in active context. Shape the work so the system does not need to.

That leads to **shorter loops rather than giant uninterrupted runs**. Explicit task state helps: the goal, the constraints, what has already been tried, what remains unresolved, and what would count as success. Clean handoffs help more than endless scrollback. Retrieval should surface the few pieces of information that matter for the current step instead of replaying the entire history. **Verification matters because sounding done is not the same thing as being done.** Fresh starts matter once a thread becomes polluted with too much stale state.

Those practices sound familiar because they are familiar. Clear goals, small tasks, good notes, fewer moving pieces, resets, and independent review also improve human work. Better outcomes usually come less from demanding that a mind try harder and more from arranging the work so success is easier.

## What this changes about how I see people

The most interesting part of this for me is not really about AI. Working with agents keeps pushing me back toward a different view of human performance.

Strong performance is often described as if it comes mainly from personal traits such as intelligence, motivation, grit, or discipline. Those traits matter, but they do not explain everything. Environment matters a great deal. Clear framing helps. Explicit expectations help. Easy access to the right information helps. Fast feedback helps. Good tools help. Reduced hidden state helps. Fewer things to actively juggle at once helps.

None of that is a sign of weakness. That is what bounded cognition looks like in practice. Agents make this easier to notice because the failure modes are stripped down and easier to see. Drift becomes obvious. Forgotten constraints become obvious. Premature declarations of success become obvious. Human versions of the same problem are often quieter, but not fundamentally different.

Some cases that look like carelessness are really overload. Some cases that look like poor judgment are really missing state. Some cases that look like motivation problems are really design problems.

## Bigger context is not better memory

A question that keeps coming up is whether AI simply needs more context. I do not think that is enough.

Human cognition does not work through giant active memory either. The mind operates more like a small workspace sitting on top of a large, messy retrieval system. Chunking, retrieval, compression, selective attention, and resets do a lot of the real work. Full replay of all relevant history is not how people make decisions.

That is why a lot of the next gains in agent performance seem more likely to come from memory systems around the model rather than from a larger buffer inside the model. Context structuring, indexing, retrieval, task state, and verification all matter because the hard problem is not storing more. The hard problem is bringing back the right few things at the right moment in a form that the system can actually use.

That direction sounds less glamorous than a headline about smarter models, but it may matter just as much in practice.

## What working with agents is teaching me

> The deeper lesson is that intelligence is not only something inside a mind. Intelligence also depends on the scaffolding around the mind.

A good agent harness does more than provide information. The harness determines what is visible, when it becomes visible, how it is shaped, and how progress gets checked. A good workplace does something similar for people. Better structure lowers cognitive overhead, reduces hidden state, creates useful feedback loops, and makes self-deception harder.

That has changed the question I ask when an agent looks lazy. Instead of asking only whether the model is smart enough, I find myself asking whether the task has been shaped in a way that **any bounded mind could handle reliably**.

That feels like a better question for AI, and a fairer question for people. The strongest takeaway has not been about superintelligence. The strongest takeaway has been about notebooks, checklists, clean interfaces, explicit goals, and the ordinary systems that protect human thinking from overload.

The more I work with agents, the less I believe intelligence is mostly raw brainpower. Good structure turns out to matter much more than I used to think.
