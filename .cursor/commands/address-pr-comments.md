# Address PR Comments

1. Check out the PR branch:
   ```bash
   gh pr checkout <PR_ID>
   ```

2. Get all comments on the PR:
   ```bash
   gh api --paginate repos/<owner>/<repo>/pulls/<PR_ID>/comments | \
     jq '.[] | {user: .user.login, body, path, line, original_line, created_at, in_reply_to_id}'
   ```

3. Also get review-level comments (not inline):
   ```bash
   gh api repos/<owner>/<repo>/pulls/<PR_ID>/reviews | \
     jq '.[] | {user: .user.login, state, body}'
   ```

4. For EACH inline comment, do the following. Address one comment at a time:
   a. Print: `"(index). From [user] on [file]:[lines] — [body]"`
   b. Read the file and the relevant line range.
   c. If you don't understand the comment, do NOT make a change. Ask for clarification.
   d. If you can address it, make the change BEFORE moving to the next comment.
   e. After making the change, verify it doesn't break existing tests:
      ```bash
      python -m pytest tests/ -x -q
      ```

5. After all comments are processed, run the full test suite:
   ```bash
   python -m pytest tests/ -q
   ```

6. Commit all changes with a descriptive message:
   ```bash
   git add -A
   git commit -m "fix: address PR review comments

   Addresses: #<PR_ID>
   - [summary of each change]"
   ```

7. Push the changes:
   ```bash
   git push origin <branch_name>
   ```

8. Summarize what you did, and which comments need the USER's attention or clarification.
