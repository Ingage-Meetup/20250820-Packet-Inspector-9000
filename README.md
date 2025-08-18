# C3ProjectTemplate

See solutions in different languages in the "Templates" directory. Once you decide which language you'd like to use,
simply open that directory in your favorite IDE, and you should be able to run the included unit tests "out of the box".

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
