# Packet Inspector 9000

## Scenario

You're helping build the validation core for **Packet Inspector 9000** — a system that filters incoming packet IDs before they’re processed by a secure data pipeline.

Each packet ID is a non-negative integer, but not all are valid. A packet passes the **Digit Integrity Check (DIC)** if:

> The packet ID can be evenly divided by the **sum of its digits**.

### Examples
- `18` passes → digit sum is `9`, and `18 ÷ 9 = 2` (whole number)
- `19` fails → digit sum is `10`, and `19 ÷ 10 = 1.9` (not whole)

Your task is to implement the logic to validate packets, scan a range of IDs, and optionally provide insights and advanced filtering.

---

## Core Requirements

Build these features using **test-driven development**:

1. **Digit Integrity Validator**
   - A function that takes an integer and returns whether it passes the DIC.
   - Write tests for typical and edge cases.

2. **Bulk Packet Filter**
   - Given an upper limit `max`, return all valid packet IDs from `0` to `max`.
   - Ensure your tests verify the contents and count of valid packets.

3. **Simple Interface**
   - Accept input for `max` and return or print the valid packet IDs.
   - Keep this logic separate so it can be mocked or swapped easily.

---

## TDD Guidelines

- Follow the **red-green-refactor loop**
- Start with the **simplest failing test**
- Cover edge cases like `0`, `1`, large numbers
- Refactor only after tests pass
- Use **mocking/stubbing** for I/O or streaming behavior if helpful

---

## Stretch Goals

Tackle any of these if time allows or to level-up the challenge:

| Goal | Description |
|------|-------------|
| **Prime Quotient Filter** | Only allow packets where `(packet ID ÷ digit sum)` is a prime number |
| **Performance Boost** | Can your code handle 1,000,000 IDs in under 1 second? |
| **Custom Base Support** | Allow digit-sum validation in bases 2–16 (default: base 10) |
| **Streaming Mode** | Build a generator that yields valid packets one at a time |
| **Diagnostics Mode** | Report stats like valid %, common digit sums, etc. |
| **UI / Web Interface** | Wrap your code in a CLI tool, API, or web page |
| **Test Coverage Report** | Use tools to report code/test coverage (language dependent) |

---

## Deliverables

By the end of the kata, aim to have:

- A clean, well-tested DIC validator and packet filter
- Clear and readable test cases
- At least one implemented stretch goal (if time allows)
- Separation of logic and input/output (mockable and testable)
- Bonus: Performance diagnostics or visualizations


## Duplicating this Repo

To create a duplicate repository from this one, follow these steps:

1. Create your new repository. For example, MyNewRepo.

2. Open Git Bash.

3. Create a bare clone of the repository.

    ```
    git clone --bare https://github.com/Ingage-Meetup/MyNewRepo.git
    ```

4. Mirror-push to the new repository.
  
    ```
    cd MyNewRepo.git
    git push --mirror https://github.com/Ingage-Meetup/MyNewRepo.git
    ```

5. Remove the temporary local repository you created earlier.

    ```
    cd ..
    rm -rf OLD-REPOSITORY.git
    ```

Your new repository now contains a mirror of this repo.

The recommended IDEs are as follows, but feel free to use whatever IDE you are comfortable with.

-   [C#](Templates/C%23) - [Microsoft Visual Studio](https://visualstudio.microsoft.com/vs/community/)
-   [Java](Templates/Java) - [IntelliJ Idea](https://www.jetbrains.com/idea/download) (Community Edition is fine)
-   [JavaScript](Templates/JavaScript) - [Microsoft Visual Studio Code](https://code.visualstudio.com/)
-   [Kotlin](Templates/Kotlin) - [IntelliJ Idea](https://www.jetbrains.com/idea/download) (Community Edition is fine)
-   [Python](Templates/Python) - [Pycharm](https://www.jetbrains.com/pycharm/download/?section=windows) (Community Edition is fine)
-   [TypeScript](Templates/TypeScript) - [Microsoft Visual Studio Code](https://code.visualstudio.com/)
