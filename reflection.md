1. Which issues were easiest and hardest to fix?

Easiest: Replacing except: with specific exceptions.

Hardest: Handling mutable default arguments since I had to redesign the function logic slightly.

2. Any false positives?

Pylint flagged stock_data as a global variable, but it’s necessary for shared state — not really an issue.

3. How would you integrate these tools in real projects?

Integrate into CI/CD pipelines (GitHub Actions) to auto-check pull requests.

Run Flake8 and Bandit locally before commits using pre-commit hooks.

4. Improvements observed:

Code became cleaner, safer, and more readable.

Eliminated hidden bugs and insecure patterns (eval, broad except).

Easier debugging due to structured logging.