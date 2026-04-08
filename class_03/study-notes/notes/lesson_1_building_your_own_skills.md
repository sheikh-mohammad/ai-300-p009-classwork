# Study Notes: Building Your Own Skills

## Executive Summary

This lesson facilitates the transition from theoretical understanding of skills to practical implementation within the Claude Code environment. The instructional content emphasizes that skill creation is fundamentally accessible, requiring only proficiency in Markdown and YAML syntax rather than advanced programming expertise. Participants will develop a functional skill within the `.claude/skills/` directory structure, learning to encode procedures through SKILL.md files that contain YAML frontmatter (configuration metadata) and Markdown-based procedural instructions. The lesson introduces the critical concept of skill activation through description fields, demonstrates the complete skill creation workflow, and establishes iterative refinement methodologies through co-learning cycles. Understanding these foundational principles enables practitioners to create reusable intellectual property that compounds in value through integration with custom agents and larger systems.

---

## Key Terms and Definitions

**Skill**: An encoded procedure or workflow documented in Markdown format with YAML frontmatter that enables Claude to perform specialized tasks consistently and reliably across multiple invocations.

**YAML Frontmatter**: Structured metadata delimited by triple hyphens (`---`) at the beginning of a skill file, containing essential configuration information including name, description, and behavioral flags that govern skill execution.

**SKILL.md**: The required Markdown file within a skill folder containing both YAML frontmatter (configuration) and procedural instructions; the singular required component for skill functionality.

**Activation Trigger**: The mechanism by which Claude determines skill relevance to user requests, primarily determined by the skill's description field which is evaluated at initialization.

**Disable-Model-Invocation**: A YAML configuration flag (`disable-model-invocation: true`) that prevents Claude from automatically invoking a skill, restricting invocation exclusively to explicit user commands; essential for skills with real-world consequences.

**User-Invocable**: A YAML parameter (`user-invocable: false`) that controls whether a skill appears in the command menu; when set to false, the skill informs Claude's behavior without appearing as an explicit command option.

**Description Formula**: A structured approach to writing skill descriptions following the pattern: [Action verb] + [input type] + [into/for] + [output type] + [key features]. Use when [trigger conditions].

**Co-Learning Cycle**: An iterative refinement methodology comprising three phases: (1) AI as Teacher (Claude suggests improvements), (2) Human as Teacher (user specifies constraints), and (3) Convergence (refinement through usage feedback).

**Skill Budget**: A character allocation (approximately 2% of context window) shared among skill descriptions; when exceeded, some skills are silently excluded from Claude's discovery mechanism.

---

## Main Content

### Part 1: Skill Architecture and File Structure

#### Directory Organization

Skills operate within a minimalist directory structure intentionally designed for accessibility:

```
.claude/skills/skill-name/
└── SKILL.md    ← Required file
```

This structure enables individuals without advanced technical backgrounds to create functional skills. A single Markdown file constitutes a complete, operational skill.

#### SKILL.md Composition: Two Essential Parts

**Part 1: YAML Frontmatter (Configuration)**

The frontmatter section, delimited by triple hyphens, contains metadata governing skill behavior:

```yaml
---
name: "meeting-notes"
description: "Transform meeting transcripts or raw notes into structured summaries with action items, decisions, and follow-ups. Use when user shares meeting content or asks for meeting notes."
---
```

Essential fields:
- `name`: Identifier for the skill (used in command invocation via `/skill-name`)
- `description`: Activation trigger determining when Claude applies the skill

**Part 2: Markdown Body (Procedural Instructions)**

The Markdown section provides explicit, sequential instructions for skill execution:

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
```

### Part 2: Advanced Configuration for High-Impact Skills

#### Skills with Real-World Consequences

Skills performing actions with tangible consequences (code deployment, message transmission, version control operations) require the `disable-model-invocation: true` flag:

```yaml
---
name: "deploy-production"
description: "Deploy the current branch to production..."
disable-model-invocation: true
---
```

**Rationale**: Without this flag, Claude may inadvertently trigger the skill during conversation, potentially resulting in unintended consequences such as accidental production deployments or unintended system modifications.

The related field `user-invocable: false` completely removes the skill from the command menu while allowing it to inform Claude's behavior in background contexts.

### Part 3: The Description Field as Activation Mechanism

The description field functions as the primary determinant of skill activation. Claude evaluates skill descriptions at initialization to identify applicable skills for user requests.

#### Description Quality Analysis

**Ineffective Description (Overly Vague):**
```
description: "Helps with notes"
```
*Problem*: Ambiguous terminology prevents reliable activation; "notes" could reference meeting notes, study notes, or general documentation.

**Ineffective Description (Overly Narrow):**
```
description: "Summarizes Zoom meeting transcripts from the marketing team"
```
*Problem*: Fails to activate for alternative meeting platforms (Teams, Google Meet) or non-marketing departmental contexts.

**Effective Description (Clear Context and Action):**
```
description: "Transform meeting transcripts or raw notes into structured summaries with action items, decisions, and follow-ups. Use when user shares meeting content or asks for meeting notes."
```

**Success Factors:**
- Specifies action verb (transform)
- Identifies input types (transcripts or raw notes)
- Enumerates key outputs (action items, decisions, follow-ups)
- Defines activation conditions (meeting content, meeting notes requests)

#### The Description Formula

```
[Action verb] + [input type] + [into/for] + [output type] + [key features].
Use when [trigger conditions].
```

**Exemplars:**

1. **Blog Planning**: "Plan blog posts with topic research, outline creation, headline variations, and introduction drafts. Use when user asks to plan, outline, or write blog content."

2. **Code Review**: "Perform systematic code reviews checking security, performance, maintainability, and best practices. Use when user asks to review code or check for issues."

3. **Email Drafting**: "Draft professional emails matching specified tone and purpose. Use when user needs to write emails or requests communication help."

### Part 4: Practical Implementation Workflow

#### Step 1: Directory Creation

```bash
mkdir -p .claude/skills/blog-planner
```

#### Step 2: SKILL.md File Development

Create `.claude/skills/blog-planner/SKILL.md` with complete configuration and procedures:

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

#### Step 3: Skill Validation

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

#### Step 4: Activation Verification

Explicitly query skill activation:

```
What skills are you using in our conversation? Did you activate the blog-planner skill?
```

### Part 5: Iterative Refinement Through Co-Learning

Initial skill versions require refinement through systematic iteration. The co-learning cycle facilitates continuous improvement through collaborative human-AI interaction.

#### Phase 1: AI as Teacher

Request Claude's assessment of skill effectiveness:

```
Review my blog-planner skill. What could be improved?
Suggest 2-3 specific enhancements.
```

Claude might suggest:
- Add SEO considerations to the outline section
- Include word count targets for each section
- Add a "common mistakes to avoid" section

#### Phase 2: Human as Teacher

Specify constraints and preferences that Claude may not independently recognize:

```
Good suggestions, but I have constraints:
- Headlines must be curiosity-driven, NEVER clickbait
- I prefer problem → insight → application structure
- Keep introductions under 100 words

Update the skill with these constraints.
```

#### Phase 3: Convergence

Refine through accumulated usage feedback:

```
I've used the blog-planner skill 3 times now. Here's what worked and what didn't:
- Worked: Headline variations are excellent
- Didn't work: Outlines are too generic, need more specific section descriptions

Help me update the skill to fix the outline issue.
```

### Part 6: System Integration and Architectural Considerations

#### Commands and Skills Convergence

The commands system (`.claude/commands/`) and skills system (`.claude/skills/`) now operate as unified infrastructure. Files in either location create equivalent `/command` invocations. The skills system represents the current standard approach for new skill development.

#### Skill Budget Constraints

When multiple skills are installed, Claude may not discover all of them due to character budget constraints (approximately 2% of context window). Skill descriptions share this budget; when capacity is exceeded, some skills are silently excluded from Claude's discovery mechanism.

**Diagnostic Command:**
```
/context
```

This command displays warnings regarding excluded skills. If exclusions occur, consider removing unused skills or abbreviating descriptions to optimize budget allocation.

#### Broader Implications for System Architecture

Skills created through this process become foundational components for larger systems. In subsequent instructional modules, custom agents developed through SDKs will integrate these skills directly, creating compounding value through reusable intellectual property that scales across multiple applications and contexts.

---

## Review Questions

### Definitional Questions (Testing Recall)

1. **Define YAML frontmatter and identify its essential fields in a SKILL.md file.** What information does frontmatter contain, and why is it necessary for skill functionality?

2. **What is the purpose of the `disable-model-invocation: true` flag, and in what contexts should it be employed?** Provide an example of a skill that would require this flag.

### Conceptual Questions (Testing Understanding)

3. **Explain why the description field is considered the most critical component of a skill's configuration.** How does the description field determine skill activation, and what consequences result from ineffective descriptions?

4. **Compare and contrast the three description examples (vague, narrow, and effective) presented in the lesson.** What specific elements make the effective description superior for Claude's activation mechanism?

5. **Describe the co-learning cycle and explain how each phase (AI as Teacher, Human as Teacher, Convergence) contributes to skill refinement.** Why is iterative refinement preferable to attempting perfection on initial skill creation?

### Application Questions (Testing Synthesis)

6. **You have created a skill for code review with the following description: "Reviews code for issues." Using the description formula provided, rewrite this description to be more effective.** Ensure your revised description specifies action verbs, input types, output types, and activation conditions.

7. **Design a skill for your primary professional domain or academic field.** Provide: (1) the skill name, (2) an effective description using the formula, (3) three "When to Use" triggers, (4) the primary procedure steps (minimum 4), and (5) the expected output format.

### Critical Thinking Questions (Testing Analysis)

8. **Discuss the relationship between skills created in this lesson and custom agents developed through SDKs in subsequent modules.** How do skills function as building blocks for larger systems, and what advantages does this modular approach provide?

---

## Answer Guidance

**Question 1**: YAML frontmatter contains metadata delimited by triple hyphens. Essential fields include `name` (skill identifier) and `description` (activation trigger). Frontmatter is necessary because it provides Claude with configuration information required to recognize and invoke skills appropriately.

**Question 2**: The flag prevents Claude from automatically invoking skills with real-world consequences. Example: a deployment skill should require explicit user invocation to prevent accidental production deployments.

**Question 3**: The description field determines activation because Claude evaluates descriptions at initialization to identify applicable skills. Ineffective descriptions result in either over-activation (triggering inappropriately) or under-activation (failing to trigger when needed).

**Question 4**: The effective description succeeds because it specifies action verbs, identifies input/output types, enumerates key features, and defines activation conditions. Vague descriptions lack specificity; narrow descriptions fail to generalize across contexts.

**Question 5**: The co-learning cycle involves three phases: AI suggests improvements, humans specify constraints, and convergence occurs through usage feedback. This iterative approach is preferable because skills improve through practical application rather than theoretical perfection.

**Question 6**: Revised description: "Perform systematic code reviews checking security, performance, maintainability, and best practices. Use when user asks to review code, requests quality assessment, or mentions code issues."

**Question 7**: Responses will vary by domain. Effective responses should follow the description formula, provide specific activation triggers, include 4+ procedure steps, and specify clear output formats.

**Question 8**: Skills serve as reusable intellectual property that integrate directly into custom agents. This modular approach enables scalability, reusability across multiple applications, and compounding value through systematic composition of specialized capabilities.

---

## Supplementary Resources

- **Foundational Reference**: Chapter 13: Markdown for AI-Native Development
- **Practical Exercises**: Lesson 10: Agent Skills Exercises (27 hands-on exercises with one-click downloads)
- **Meta-Skill Application**: Skill-Creator skill for automated skill generation and refinement
- **System Integration**: Part 6 instructional modules on Custom Agents and SDK integration
