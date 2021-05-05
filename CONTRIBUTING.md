# Contributing to pydatagovgr
Contributions are more than welcome! Please do take a moment to read this document, in order to make the contribution process easier for everyone involved.

## Code of Conduct
It's very important to keep the library - and the open-source ecosystem in general - open and inclusive. Please read and embrace the contributor's [Code of Conduct](CODE_OF_CONDUCT.md).

## :bug: Bug Report 
- Before opening an issue, please use the Github issue tracker to check if the issue has already been reported. 
- When you are opening an issue, no need to improvise! Just [click here](https://github.com/ilias-ant/pydatagovgr/issues/new/choose) to create a new issue and select the ":bug: Bug Report" template.

## :rocket: Feature Requests
Feature requests are welcome. But do take a moment to find out whether your idea fits with the scope and aims of the project. 
Please provide as much detail and context as possible. Sounds boring? Just [click here](https://github.com/ilias-ant/pydatagovgr/issues/new/choose) to create a new issue and select the "🚀 Feature Request" template.

## :memo:	 Pull Requests
Pull requests are very welcome — be they bug fixes, improvements or new features. Before embarking on a significant pull request,
please first discuss the change you wish to make with the owners of this repository, by creating an [issue](https://github.com/ilias-ant/pydatagovgr/issues/new/choose).

Please make sure your PRs adopt the following practices:
- Are limited to a single feature/issue
- Have a clear title and description
- Features or bug fixes **must be tested** by one or more unit-tests
- Public API methods (aka made to be accessible by the end-user) **must** be thoroughly documented
- Code is properly styled and formatted and adheres to the design principles - library draws inspiration from the [black](https://github.com/psf/black) style
- are comprised of clean and meaningful Git commits - see the section below for more details on this

## Commits
To enable a linear, clean and intuitive Git history, here are some basic suggestions and guidelines to keep in mind before making your first commit:

Each commit message should ideally consist of a **header**, a **body**, and a **footer**.

```
<header>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

The **header** is mandatory and should strictly have the following format:

```
[<type>]: <summary>
```

where: `<summary>` delivers a clear, concise description of the respective change in less than 50 characters and`<type>` must be one of the following:

* **build**: Changes that affect the build system or external dependencies (examples: Github Actions, poetry.lock, pyproject.toml)
* **docs**: Documentation only changes (examples: README, CONTRIBUTING)
* **feat**: A new feature
* **fix**: A bug fix
* **perf**: A code change that improves performance
* **refactor**: A code change that neither fixes a bug nor adds a feature
* **test**: Adding missing tests or correcting existing tests

(if you are a battle-hardened developer and the above types seem familiar, you're right - they are heavily based on the excellent work of the [Angular](https://github.com/angular/angular) community)

The **body** is an optional element of a commit message - can be added when you want to better document the reasoning behind the change.

Lastly, the **footer** should strictly be reserved for referencing issues, other pull requests etc.


For example, a typical commit could be:

```
[feat]: added rate-limiter to the DataGovClient

Requests dispatched from the client towards data.gov.gr API now obey a rate-limit. 
This ensures that API is not "hammered' at any given moment.

closes #4242
```

## What are you talking about 😕? 
If you are not familiar with the Github contributing process and all the above sound gibberish, despair not! You can always take a look at [this very practical guide](https://github.com/firstcontributions/first-contributions). If again this does not help, please do contact me via email or via the issue tracker and i will be glad to help in any way!

Thank you! :heart: 

---

:point_up: By submitting work for inclusion to this project, you agree to allow the project owner to license your work 
under the same license as that used by the project.
