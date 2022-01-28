# Experimental 
Tested for **pyenv**

## Behave pre-commit hook
If there are unused steps this hook will shows them

## Install

Add the following lines in your **.pre-commit-config.yaml** file.

bash
```
  - repo: https://github.com/celltrak/behave_hook
    rev: HEAD
    hooks:
      - id: behave-unused-steps
```
