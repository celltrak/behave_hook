# Experimental 
Tested only with **pyenv** 

## Behave pre-commit hook
If there are unused steps this hook will shows them

## Install

Add the following lines in your **.pre-commit-config.yaml** file.

```
  - repo: https://github.com/celltrak/behave_hook
    rev: v0.0.1
    hooks:
      - id: behave-unused-steps
```
