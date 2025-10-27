| Issue Type          | Line(s) | Description                            | Fix Approach                                            |
| ------------------- | ------- | -------------------------------------- | ------------------------------------------------------- |
| Mutable default arg | 12      | `logs=[]` shared across function calls | Change default to `None` and initialize inside function |
| Broad Exception     | 20      | `except:` hides real errors            | Replace with `except KeyError:` or specific exception   |
| Dangerous function  | 64      | `eval()` used (security risk)          | Remove `eval` or replace with safe alternative          |
| Invalid type usage  | 61      | Passing `123` and `"ten"`              | Add input validation or type check                      |
