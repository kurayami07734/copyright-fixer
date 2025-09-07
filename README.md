# Copyright Fixer 

CLI to keep the copyright notices updated automatically

## Steps to run locally

1. create a test git repo at the same level as this project

```bash
cd ..
mkdir test-git-repo
cd test-git-repo
git init .
```

2. setup pre-commit (This may require setting up venv with pre-commit)

```bash
pip install pre-commit
```

3. Add .pre-commit-config.yaml 

```yaml
repos:
  - repo: ../copyright-fixer
    rev: <latest_commit_hash>
    hooks:
       - id: copyright-fixer
         args: ["-n", "Acme, Inc.", "-s", "#"]
```

4. install pre-commit hash

```bash
pre-commit install
```

5. run pre-commit 
```bash
pre-commit run --verbose
```

### Note

Everytime you make any changes, commit them and update the `rev` in `.pre-commit-config.yaml`
Stage the change in the `.pre-commit-config.yaml` and then run the pre-commit