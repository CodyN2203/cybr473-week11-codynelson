# CYBR 473 — Violent Python — Submission Guidelines

These guidelines apply to **every** assignment in this course, whether or not the assignment description repeats them. Read them once at the start of the term and check them before each submission.

---

## How to submit your work

You create and own your repository for every assignment.

1. **Create your repository from the assignment template.** Open the template link posted in D2L and choose **Use this template → Create a new repository**.
2. **Name the repository exactly as the assignment specifies.** The required form is `cybr473-weekN-yournetid`, where `N` is the assignment number and `yournetid` is your UA NetID (for example, `cybr473-week1-jsmith`). This is a requirement, not a suggestion: submissions are collected and checked in bulk by repository name, and a repository that does not follow the convention may not be picked up for grading.
3. **Set the repository to Private.** Never make graded work public.
4. **Invite your instructor as a collaborator**, using the GitHub username listed in D2L. Work the instructor cannot open cannot be graded.
5. **Clone the repository in PyCharm** with **Get from Version Control**.
6. **Commit meaningfully as you work.** Several small commits with clear messages, not one large commit at the end. Your commit history is part of what is graded.
7. **Submit the repository URL in D2L.** Pushing to GitHub without submitting the link in D2L does not count as submitting.

If you cannot access the template, contact the instructor before the due date.

---

## 1) Include a header at the very top of your script

Include your name, the date, and the course name and number.

---

## 2) Keep the file structure consistent with Python best practices

Most assignments come with the structure already built. Use it.

Anyone should be able to find your script and your documents without hunting.

- Scripts go in `scripts/` or `src/`.
- Screenshots, output, and written reflections go in `docs/`.
- Assets go in `assets/`, `images/`, or something appropriately named such as `dumps/`.

Written reflections must be Markdown (`.md`) files, not `.docx` or `.pdf`. Markdown renders cleanly on GitHub, keeps formatting consistent, and avoids clutter from proprietary file types.

Do not drop your work at the root of the project. Keep it clean and organized.

---

## 3) Add `requirements.txt` at the root when you use third-party modules

See [the pip requirements file format](https://pip.pypa.io/en/stable/reference/requirements-file-format/) for details.

---

## 4) Include and edit the README when needed

If running your script is not as simple as running a Python file, include instructions.

---

## 5) Follow Python best practices when coding

Assignments may not call this out specifically, but it is expected in an upper-division Python course.

At a minimum:

- Do not use absolute paths.
- Catch exceptions elegantly.
  - Stop the script if an exception breaks it, and give reasonable feedback.
  - The script should not crash on bad input.
- Account for multiple test cases, at a minimum:
  - Data too large to process
  - Data too small to process
  - Data that does not exist
  - Data that is misformatted
  - Data in the wrong case (capital vs. lower)
  - Data that is not consistently formatted
  - Data formatted in more than one reasonable way
    - For example, locations may appear as:
      - Tucson
      - Tucson, Arizona
      - Tucson, AZ
      - Tucson, Arizona USA
    - Either state a specific required input format or account for the reasonable cases.
  - For numeric input, handle:
    - Negative numbers
    - Very small numbers
    - Very large numbers
    - Zero
    - Non-digits and symbols
    - Decimals, integers, floats (`e` or pi included)
- Sanitize input reasonably.
  - Strip trailing spaces.
  - Remove unsupported or script-breaking characters.
- Never commit credentials or API keys. Use environment variables or secrets.

**Note:** Your scripts will be evaluated with both the provided test data and additional edge-case data, to assess how well your code handles unexpected or extreme input. The only exception is when you can always guarantee how data passes through your code: say so in your comments.

**The above are required as a minimum.**

There are many more Python best practices, such as:

- Testing
- Type hints
- Example `.env` files
- The `logging` module

Use them as you see fit.

---

## 6) Use comments

Comment where it is unclear what a snippet does, and to explain your reasoning and decisions.

---

## 7) Every assignment needs evidence that your script ran

Attach proof that your script ran correctly to every submission: a screenshot, a video recording, and/or a CSV. Sometimes the assignment names the format. When it does not, include the best evidence at your discretion.

Video submissions must be `.mp4` or `.mov`. Uploads to any outside service, such as YouTube, are not acceptable. Submit the video in the repository or directly to D2L. Videos in another format or hosted elsewhere will not be graded.

---

## 8) Never commit secrets

Do not commit API keys, passwords, or anything you would not want the entire world to see. Committed secrets carry a steep penalty. Use environment variables or another secrets-management method. Even prompting for a secret is better than hardcoding it.

---

## 9) Always submit the repository URL in D2L

The D2L submission is what gets graded. Make sure the instructor has been invited as a collaborator on the repository before you submit the link. A private repository the instructor cannot open will be treated as unsubmitted.

---

## 10) Call out any AI usage or outside sources

Per the syllabus academic integrity policy, code copied from the internet, from AI tools, or from any other outside source must not be submitted, whether or not you cite it. Citing a source does not make copied code acceptable. The only code you may reuse directly is example code the instructor has explicitly provided.

If an outside resource (a Stack Overflow thread, documentation, an AI tool) helped you *understand* something before you wrote your own code, disclose it with a comment describing how, why, and to what extent you used it:

```python
# I wasn't sure what csv.DictReader actually returns, so I referenced this
# StackOverflow thread: https://stackoverflow.com/questions/74853214/understanding-csv-dictreader-what-it-returns

# ChatGPT helped me understand how to sort a list of dictionaries by a
# specific value; I wrote the implementation below myself after that.
# (ChatGPT, Jan 1, 2025) [Link to Conversation Here]
```

By submitting your work you are claiming it is entirely your own unless you have disclosed otherwise as described above. See the [AI Usage Guidelines](https://d2l.arizona.edu/d2l/common/dialogs/quickLink/quickLink.d2l?ou=1801706&type=content&rcode=Arizona-13393589) for details.

---

## 11) Deviating from course content

Exploring packages, tools, or approaches beyond what is covered in class is fine. Curiosity is a good thing. But stick to the spirit of the examples and the course content when solving assignments; this course is built around a specific set of tools and techniques for a reason.

Any deviation from course content, such as a package or import not discussed in class or in the examples, requires a detailed explanation in your submission.

If you want to explore a different solution or tool, reach out first. I am happy to talk it through with you.
