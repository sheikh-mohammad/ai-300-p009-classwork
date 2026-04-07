# Markdown Basics Guide

## 1. Headings
Headings are created using `#` symbols. More `#` symbols = smaller heading.

```markdown
# Heading 1 (Largest)
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6 (Smallest)
```

**Use case**: Organize your document into sections and subsections.

---

## 2. Text Formatting

### Bold
Use `**text**` or `__text__` to make text bold.
```markdown
**This is bold** or __this is bold__
```

### Italic
Use `*text*` or `_text_` to make text italic.
```markdown
*This is italic* or _this is italic_
```

### Bold + Italic
Use `***text***` for both.
```markdown
***This is bold and italic***
```

### Strikethrough
Use `~~text~~` to strike through text.
```markdown
~~This is crossed out~~
```

---

## 3. Lists

### Unordered Lists
Use `-`, `*`, or `+` to create bullet points.
```markdown
- Item 1
- Item 2
  - Nested item 2.1
  - Nested item 2.2
- Item 3
```

### Ordered Lists
Use numbers followed by a period.
```markdown
1. First item
2. Second item
   1. Nested item 2.1
   2. Nested item 2.2
3. Third item
```

### Checklists
Use `- [ ]` for unchecked and `- [x]` for checked items.
```markdown
- [x] Completed task
- [ ] Pending task
- [ ] Another pending task
```

---

## 4. Links

### Basic Link
```markdown
[Link text](https://example.com)
```

### Link with Title
```markdown
[Link text](https://example.com "Hover text")
```

### Reference Link
```markdown
[Link text][reference]

[reference]: https://example.com
```

---

## 5. Images

### Basic Image
```markdown
![Alt text](image-url.jpg)
```

### Image with Link
```markdown
[![Alt text](image-url.jpg)](https://example.com)
```

---

## 6. Code

### Inline Code
Use backticks for code within text.
```markdown
Use the `console.log()` function to print output.
```

### Code Blocks
Use triple backticks with optional language specification.

```markdown
```python
def hello_world():
    print("Hello, World!")
```
```

Supported languages: `python`, `javascript`, `java`, `cpp`, `html`, `css`, `sql`, etc.

---

## 7. Blockquotes

Use `>` to create blockquotes.
```markdown
> This is a blockquote.
> It can span multiple lines.

> This is a nested blockquote.
>> Even deeper nesting.
```

---

## 8. Horizontal Line

Use `---`, `***`, or `___` to create a horizontal line.
```markdown
---
```

---

## 9. Tables

Create tables using pipes `|` and dashes `-`.
```markdown
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Row 1    | Data     | Value    |
| Row 2    | Data     | Value    |
```

Alignment:
- Left align: `|---|`
- Center align: `|:-:|`
- Right align: `|-:|`

```markdown
| Left | Center | Right |
|:-----|:------:|------:|
| L    | C      | R     |
```

---

## 10. Escape Characters

Use backslash `\` to escape special markdown characters.
```markdown
\# This won't be a heading
\*This won't be italic\*
```

---

## 11. Line Breaks

Add two spaces at the end of a line or use `<br>` for a line break.
```markdown
Line 1  
Line 2

Or use HTML:
Line 1<br>Line 2
```

---

## 12. Comments

HTML comments won't display in rendered markdown.
```markdown
<!-- This is a comment and won't show up -->
```

---

## Quick Reference Cheat Sheet

| Element | Syntax |
|---------|--------|
| Heading | `# Heading` |
| Bold | `**bold**` |
| Italic | `*italic*` |
| Link | `[text](url)` |
| Image | `![alt](url)` |
| Code | `` `code` `` |
| Code Block | ` ```code``` ` |
| List | `- item` |
| Ordered List | `1. item` |
| Blockquote | `> quote` |
| Horizontal Line | `---` |
| Table | `\| col1 \| col2 \|` |

---

## Tips for Using Markdown in Software Engineering

1. **Version Control**: Markdown files work great with Git — easy to track changes
2. **Readability**: Plain text format is readable even without rendering
3. **Portability**: Works on any platform, any text editor
4. **Documentation**: Perfect for README files, API docs, and project guides
5. **Collaboration**: Easy to share and collaborate on via GitHub, GitLab, etc.
