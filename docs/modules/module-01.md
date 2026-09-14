# Module 1 — Orient in an existing system

**Session:** 1 — 14 September 2026
**Deadline:** Friday 25 September 2026, 20:00 Riga time (UTC+3)
**Submit:** repository URL + commit SHA, in Evaluentis (https://evaluatentis.leitass.eu)

---

## Goal

Take a five-part system in four languages that you did not write, get it running on your own machine, and be able to explain how a single request travels through it.

There is no feature to build in this module. That is deliberate. Everything you do from Module 2 onward depends on you being able to find your way around this codebase, and that skill is worth a module of its own.

---

## What the template already gives you

Everything. The system runs as it is:

- `frontend` — Vanilla JS + Vite
- `products-service` — PHP / Slim
- `users-service` — Python / FastAPI
- `orders-service` — Java / Spring Boot
- `postgres` — PostgreSQL, with a Prisma migration runner

The stack is wired end to end, but the functionality is deliberately thin. The migration runner creates the schema and seeds sample data. Each service exposes one read-only endpoint (`GET /products`, `GET /users`, `GET /orders`), and the frontend fetches all three and renders them as lists. Nothing creates, edits or deletes data yet.

---

## What you must add

No production code this module.

You add a working environment, your first commits, and documentation that only someone who ran the system could have written.

---

## Definition of done

All four items below, committed to your fork, at the SHA you submit.

### 1. `docs/exploration/01-system-map.md`

**a. Your own diagram.** Draw the system yourself — the five parts, what talks to what, and in which direction. ASCII, Mermaid, or a photograph of a whiteboard are all acceptable. A copy of the diagram in the README is not: the point is that you have built the picture in your own head.

**b. One request, traced end to end.** Pick one request the application makes. For each hop, give the `file:line`:

- the frontend file and line that issues the request
- the URL and the service that receives it
- the route or controller that matches it
- the query or ORM call that runs, and the table it touches
- the frontend function that turns the response into DOM

**c. Environment gotchas.** Every error, warning or surprise you hit while getting the system running, and what fixed it. If nothing went wrong, say so and record how long the build took.

**d. One thing the documentation gets wrong or leaves out.** The README or `ARCHITECTURE.md` contains at least one statement that is stale, incomplete or misleading. Find one, quote it, and say what is actually true.

Item (d) is not a trick and not a criticism of the repo — every real codebase drifts from its documentation. Noticing that drift is the skill.

### 2. `reflections/module-01.md`

Use the template in the repo. Required headings, all non-empty:

- What I did
- What I did not understand at first
- What I would do differently
- How long this took me

Never scored on quality. Required to be present, honest and non-empty.

### 3. Evaluentis self-check

Seven questions, about ten minutes. Completion is the requirement; the score does not enter your grade.

### 4. Commit history

At least three commits, on at least two different days, with messages that describe the change. One commit called "module 1" on the deadline satisfies nothing and will generate a question at the exam.

---

## What I will teach

In session 1, in the room:

- how the five parts are wired together, and what Docker Compose does to connect them
- one request traced live, end to end
- how this course is assessed, in full

That is all. The rest is below.

---

## What you research yourself

Five questions. Each answer should be short, specific to **this** repository, and something you could say out loud without reading.

1. What does `docker compose up` actually do, step by step, for this compose file?
   *A good answer names the stages in order and says what happens on the second run that did not happen on the first.*

2. How does one container reach another by name? What resolves that name?
   *A good answer explains why `http://products-service:xxxx` works inside the network and not from your browser.*

3. Container, image, volume — which of the three keeps your data across a restart, and which throws it away?
   *A good answer says what happens to the database after `docker compose down` versus `docker compose down -v`.*

4. What does the Prisma migration runner do here, and why is it a separate container rather than part of a service?
   *A good answer covers who owns the schema when three services share one database.*

5. Why is this system written in four languages? Give one real benefit and one real cost.
   *A good answer resists both "microservices are good" and "this is over-engineered", and talks about what it costs a team.*

**These questions are the source of exam questions.** They are not homework padding.

---

## How this is assessed

| Deliverable | Where it counts |
| --- | --- |
| All four done-items present | Admission hurdle — pass/fail, no points |
| Your system map and request trace | Exam: code defence questions are built on your ability to navigate |
| Your research answers | Exam: the concept questions come from here |
| Commit history | Exam: engineering practice component |

Nothing in this module is scored on its own. All of it is what makes the exam survivable.

---

## Deadline and submission

1. Commit and push everything to your fork
2. `git rev-parse HEAD` — copy the SHA
3. Submit the fork URL and that SHA in Evaluentis, Module 1
4. Complete the Module 1 self-check in Evaluentis

**Due Friday 25 September 2026, 20:00 Riga time (UTC+3).** Late means not yet admitted, not a lower grade. Submit and it clears.

---

## If you are stuck

Bring the error message. Not "it doesn't work" — the actual output, and what you tried.

Stuck for more than 30 minutes on environment setup is not perseverance, it is wasted time. Ask.
