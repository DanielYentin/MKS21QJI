# how-to :: Markdown Syntax
---
## Overview
Markdown is a basic syntax used for formatting simple text. It allows for a multitude of text manipulation, such as size and formatting. Many common word processors such as Microsoft word and Google docs implement these features, but the syntax is hidden from you. Markdown allows you to specify, inline, what modifications you want to apply to your text.

### Estimated Time Cost: .3 hrs

### Prerequisites:
  1. Make a new file with a .md extension
  2. Open up an editor with markdown preview capabilities
> How to view markdown?

Many IDEs either support markdown out of the box, or have downloadable plugins/extensions that can convert your markdown into formatted text.

1. Atom supports markdown preview out of the box (ctr/cmd + shift + m)
2. VSCode supports markdown preview out of the box (ctr/cmd + shift + v)
3. Github has a preview button when editing a markdown file

#### Markdown Syntax
> What types of formatting does markdown support?

Markdown suports six diffrent font sizes, denoted by the amount of '\#' placed at the start of the line. One '\#' is the largest, while six '\#'s is the smallest.

Basic Markdown supports three other text modifications. *Italic* text can be denoted using one '\*' on both ends of a word. **Bold** text can be denoted using two '*'s on either side of a word.
~~Strikethrough~~ can be denoted with two '\~\~' on both ends of a word.

Extended Markdown supports three other modifications. ==Highlight== can be denoted with two '\=\=' on both ends of a word.

Subscript can be denoted with one '~' or a \<sub> tag(if your markdown supports HTML) separating the normal script and the subscript.

**Ex**: [H\~2\~O] ---OR--- [H\<sub>2\</sub>O] &rarr; [H<sub>2</sub>O]

Superscript can be denoted with one '^' or a \<sup> tag(if your markdown supports HTML) separating the normal script and the superscript.

**Ex**: [e\^x\^] ---OR--- [e\<sup>x\</sup>] &rarr; [e<sup>x</sup>]

Markdown also supports a number of text formatting that improves readability, but does not change the text itself.

Ordered lists can be denoted using numbers starting at 1.
1. First item
2. Second item
3. Third item
4. Fourth item

Unordered lists can be denoted using a '- ' or '* '.
- First item
* Second item
- Third item
* Fourth item

Code blocks can be denoted with backticks (\`\`) both ends of the code.

\`print("hello world")\` &rarr; `print("hello world")`



### Resources
* https://www.markdownguide.org/

---

Accurate as of (last update): 2022-10-20

#### Contributors:
Success
Ivan Yeung, pd2  
Daniel Yentin, pd2  
