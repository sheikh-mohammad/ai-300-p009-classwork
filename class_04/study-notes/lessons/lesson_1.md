# Building Your Own Skills

## Summary

This lesson facilitates the transition from theoretical understanding of skills to practical implementation. Participants will develop a functional skill within the `.claude/skills/` directory structure and acquire the competency to create additional skills independently. The instructional content emphasizes the accessibility of skill creation through Markdown-based documentation with YAML frontmatter, demonstrating that technical expertise in programming is not a prerequisite for skill development.

---

## Key Terms and Definitions

**Skill**: An encoded procedure or workflow documented in Markdown format with YAML frontmatter that enables Claude to perform specialized tasks consistently and reliably.

**YAML Frontmatter**: Structured metadata at the beginning of a skill file (delimited by `---`) that contains essential configuration information including name, description, and behavioral flags.

**SKILL.md**: The required Markdown file within a skill folder that contains both the YAML frontmatter (configuration) and the procedural instructions for skill execution.

**Activation Trigger**: The mechanism by which Claude determines whether a skill is relevant to a user's request, primarily determined by the skill's description field.

**Disable-Model-Invocation**: A YAML flag that prevents Claude from automatically invoking a skill, restricting invocation to explicit user commands; essential for skills with real-world consequences.

**User-Invocable**: A YAML configuration parameter that controls whether a skill appears in the command menu; when set to `false`, the skill informs Claude's behavior without appearing as an explicit command.

---

## Foundational Requirements

Before proceeding with skill creation, participants should possess familiarity with:

- **Markdown syntax**: Headers, bullet points, code blocks, and text formatting
- **YAML syntax**: Key-value pairs and basic data structure representation
- **Procedural documentation**: Clear, sequential instruction writing

The instructional materials recommend a 15-minute review of Markdown for AI-Native Development (Chapter 13) for participants lacking confidence in these foundational areas.

---

## Skill Architecture: The SKILL.md File Structure

### Directory Organization

Each skill resides within its own folder under `.claude/skills/`:

```
.claude/skills/meeting-notes/
└── SKILL.md    ← Required file
```

This minimalist structure intentionally prioritizes accessibility, enabling individuals without advanced technical backgrounds to create functional skills.

### Part 1: YAML Frontmatter (Configuration)

The frontmatter section, delimited by triple hyphens (`---`), contains metadata that governs skill behavior:

```yaml
---
name: "meeting-notes"
description: "Transform meeting transcripts or raw notes into structured summaries with action items, decisions, and follow-ups. Use when user shares meeting content or asks for meeting notes."
---
```

**Essential Fields:**
- `name`: Identifier for the skill (used in command invocation)
- `description`: Activation trigger that determines when Claude applies the skill

### Part 2: Markdown Body (Procedural Instructions)

The Markdown section provides explicit instructions for skill execution:

```markdown
# Meeting Notes Skill

## When to Use

- User shares a meeting transcript
- User asks to summarize meeting notes
- User mentions "action items" or "meeting summary"

## Procedure

1. Extract action items with owners and deadlines
2. Highlight decisions made (with who made them)
3. Summarize discussion points (don't transcribe verbatim)
4. Flag open questions for follow-up
5. Keep to one page maximum

## Output Format

**Action Items** (top of document)
- [ ] Task — Owner — Deadline

**Decisions Made**
- Decision: [what] — Made by: [who]

**Discussion Summary**
Brief bullets, not transcription.

**Open Questions**
- Question needing follow-up
```

---

## Advanced Configuration: Skills with Side Effects

Skills that perform actions with real-world consequences (code deployment, message transmission, version control operations) require the `disable-model-invocation: true` flag:

```yaml
---
name: "deploy-production"
description: "Deploy the current branch to production..."
disable-model-invocation: true
---
```

**Rationale**: Without this flag, Claude may inadvertently trigger the skill during conversation, potentially resulting in unintended consequences such as accidental production deployments.

The related field `user-invocable: false` completely removes the skill from the command menu while allowing it to inform Claude's behavior in the background.

---

## The Description Field: Activation Mechanism

The description field functions as the primary determinant of skill activation. Claude evaluates skill descriptions at initialization to identify applicable skills for user requests.

### Description Quality Criteria

**Ineffective Description (Overly Vague):**
```
description: "Helps with notes"
```
*Problem*: Ambiguous terminology prevents reliable activation.

**Ineffective Description (Overly Narrow):**
```
description: "Summarizes Zoom meeting transcripts from the marketing team"
```
*Problem*: Fails to activate for alternative meeting platforms or non-marketing contexts.

**Effective Description (Clear Context and Action):**
```
description: "Transform meeting transcripts or raw notes into structured summaries with action items, decisions, and follow-ups. Use when user shares meeting content or asks for meeting notes."
```

**Why This Succeeds:**
- Specifies the action verb (transform)
- Identifies input type (transcripts or raw notes)
- Enumerates key outputs (action items, decisions, follow-ups)
- Defines activation conditions (meeting content, meeting notes requests)

### The Description Formula

```
[Action verb] + [input type] + [into/for] + [output type] + [key features].
Use when [trigger conditions].
```

**Exemplars:**

- **Blog Planning**: "Plan blog posts with topic research, outline creation, headline variations, and introduction drafts. Use when user asks to plan, outline, or write blog content."

- **Code Review**: "Perform systematic code reviews checking security, performance, maintainability, and best practices. Use when user asks to review code or check for issues."

- **Email Drafting**: "Draft professional emails matching specified tone and purpose. Use when user needs to write emails or requests communication help."

---

## Practical Implementation: Creating Your First Skill

### Step 1: Directory Creation

```bash
mkdir -p .claude/skills/blog-planner
```

### Step 2: SKILL.md File Development

Create `.claude/skills/blog-planner/SKILL.md`:

```yaml
---
name: "blog-planner"
description: "Plan engaging blog posts with topic research, structured outlines, headline variations, and compelling introductions. Use when user asks to plan, outline, or write blog content."
---

# Blog Planning Skill

## When to Use This Skill

- User asks to "plan a blog post" or "write an article"
- User mentions blog topics, headlines, or content strategy
- User needs help structuring written content

## Procedure

1. **Understand the topic**: Clarify subject and target audience
2. **Create outline**: Structure into 3-5 main sections
3. **Generate headlines**: Provide 5 variations (curiosity-driven, benefit-focused, direct)
4. **Draft introduction**: Write a hook that challenges assumptions or poses a question

## Output Format

**Topic Summary**: 2-3 sentence overview
**Target Audience**: Who should read this?
**Outline**: Numbered list of main sections with brief descriptions
**Headline Options**: 5 variations
**Introduction Draft**: 1-2 paragraph hook

## Quality Criteria

- Headlines: Curiosity-driven, never clickbait
- Introductions: Challenge assumptions or pose unexpected questions
- Outlines: Problem → failed solutions → insight → application structure
- Specificity: Use numbers over vague claims
```

### Step 3: Skill Validation

Initiate Claude Code within the project directory:

```bash
claude
```

Request skill activation:

```
Help me plan a blog post about learning AI tools as a beginner
```

**Validation Checklist:**
- Does Claude follow the documented procedure?
- Does output conform to the specified format?
- Does quality align with established criteria?

### Step 4: Activation Verification

Explicitly query skill activation:

```
What skills are you using in our conversation? Did you activate the blog-planner skill?
```

---

## Iterative Refinement Through Co-Learning

Initial skill versions require refinement. The co-learning cycle facilitates continuous improvement:

### Phase 1: AI as Teacher

Request Claude's assessment:

```
Review my blog-planner skill. What could be improved?
Suggest 2-3 specific enhancements.
```

### Phase 2: Human as Teacher

Specify constraints and preferences:

```
Good suggestions, but I have constraints:
- Headlines must be curiosity-driven, NEVER clickbait
- I prefer problem → insight → application structure
- Keep introductions under 100 words

Update the skill with these constraints.
```

### Phase 3: Convergence

Refine through usage feedback:

```
I've used the blog-planner skill 3 times now. Here's what worked and what didn't:
- Worked: Headline variations are excellent
- Didn't work: Outlines are too generic

Help me update the skill to address the outline issue.
```

---

## System Integration: Commands and Skills Convergence

The commands system (`.claude/commands/`) and skills system (`.claude/skills/`) now operate as unified infrastructure. Files in either location create equivalent `/command` invocations. The skills system represents the current standard approach.

---

## Resource Constraints: Skill Budget Limitations

When multiple skills are installed, Claude may not discover all of them due to character budget constraints (approximately 2% of context window). Skill descriptions share this budget; when capacity is exceeded, some skills are silently excluded.

**Diagnostic Command:**
```
/context
```

This command displays warnings regarding excluded skills. If exclusions occur, consider removing unused skills or abbreviating descriptions.

---

## Broader Implications

Skills created through this process become foundational components for larger systems. In subsequent instructional modules, custom agents developed through SDKs will integrate these skills directly, creating compounding value through reusable intellectual property.

---

## Review Questions

1. **Definitional**: What is the primary function of the YAML frontmatter in a SKILL.md file, and what are its essential fields?

2. **Conceptual**: Explain why the description field is considered the most critical component of a skill's configuration. How does it determine skill activation?

3. **Application**: You have created a skill for code review. Your current description reads: "Reviews code for issues." Using the description formula provided, rewrite this description to be more effective.

4. **Analytical**: Compare the three description examples (vague, narrow, and effective). What specific elements make the effective description superior for Claude's activation mechanism?

5. **Synthesis**: Describe the co-learning cycle and explain how each phase (AI as teacher, human as teacher, convergence) contributes to skill refinement.

6. **Critical Thinking**: Why is the `disable-model-invocation: true` flag necessary for skills that perform actions with real-world consequences? What risks does it mitigate?

7. **Application**: Design a skill for your primary professional domain. Provide: (1) the skill name, (2) an effective description using the formula, (3) three "When to Use" triggers, and (4) the primary procedure steps.

8. **Evaluation**: Discuss the relationship between skills created in this lesson and custom agents developed through SDKs in subsequent modules. How do skills function as building blocks for larger systems?

---

## Additional Resources

- **Markdown Reference**: Chapter 13: Markdown for AI-Native Development
- **Practical Exercises**: Lesson 10: Agent Skills Exercises (27 hands-on exercises)
- **Meta-Skill Application**: Skill-Creator skill for automated skill generation
